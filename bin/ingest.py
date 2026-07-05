#!/usr/bin/env python3
"""ingest — deterministic landing of curated material into a Hugo page bundle.

    ingest.py <manifest.md> --slug <slug> --site <site-repo> \
              --root <label>=<dir> [--root <label>=<dir> ...]

Executes ticked `- [x] role path` lines from a sweep manifest:

  hero/gallery  image -> web derivative (max 1600px, jpg q85) in the bundle
  embed         `YOUTUBE <id>` -> shortcode queued for index.md; file paths
                are refused (video never enters git)
  doc           .pdf copied to bundle docs/; .md copied to bundle notes/
                (page resources, not rendered pages)

Paths resolve against the first --root whose label prefixes the line
(`notebook: foo.md`), else the first root. Scaffolds index.md with TODO
markers if absent; never overwrites bundle files that already exist.
Deterministic, idempotent, no LLM.
"""

import argparse
import os
import re
import shutil
import sys

from PIL import Image

MAX_DIM = 1600
JPG_QUALITY = 85

LINE_RE = re.compile(r"^- \[x\] (\w+)\s+(.*?)\s*(?:\(\d+[BKMGT]\))?\s*(?:#.*)?$")


def slugify(name):
    base = os.path.splitext(os.path.basename(name))[0].lower()
    return re.sub(r"[^a-z0-9]+", "-", base).strip("-")


def derive_image(src, dst):
    if os.path.exists(dst):
        print(f"  keep  {os.path.basename(dst)} (exists)")
        return
    img = Image.open(src)
    img = img.convert("RGB")
    img.thumbnail((MAX_DIM, MAX_DIM))
    img.save(dst, "JPEG", quality=JPG_QUALITY)
    print(f"  image {os.path.basename(dst)} {img.size[0]}x{img.size[1]}")


def copy_once(src, dst):
    if os.path.exists(dst):
        print(f"  keep  {os.path.basename(dst)} (exists)")
        return
    shutil.copy(src, dst)
    print(f"  copy  {os.path.basename(dst)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--site", required=True)
    ap.add_argument("--root", action="append", required=True,
                    help="label=dir; label matches 'label:' path prefixes")
    args = ap.parse_args()

    roots = []
    for spec in args.root:
        label, _, path = spec.partition("=")
        roots.append((label, os.path.abspath(path)))

    bundle = os.path.join(os.path.abspath(args.site), "content", "projects", args.slug)
    os.makedirs(bundle, exist_ok=True)

    hero = None
    gallery = []
    embeds = []
    docs = []
    links = []

    with open(args.manifest, encoding="utf-8") as f:
        for line in f:
            m = LINE_RE.match(line.strip())
            if not m:
                continue
            role, path = m.group(1), m.group(2).strip()

            if role == "link":
                links.append(path)
                continue

            if role == "embed":
                yt = re.match(r"YOUTUBE\s+(\S+)", path)
                if not yt:
                    sys.exit(f"refusing video file (upload + embed instead): {path}")
                embeds.append(yt.group(1))
                continue

            src_root = roots[0][1]
            for label, root in roots:
                prefix = label + ":"
                if path.startswith(prefix):
                    src_root, path = root, path[len(prefix):].strip()
                    break
            src = os.path.join(src_root, path)
            if not os.path.isfile(src):
                sys.exit(f"not found: {src}")

            if role in ("hero", "gallery"):
                dst = os.path.join(bundle, slugify(path) + ".jpg")
                derive_image(src, dst)
                if role == "hero":
                    hero = os.path.basename(dst)
                else:
                    gallery.append(os.path.basename(dst))
            elif role == "doc":
                sub = "notes" if path.lower().endswith(".md") else "docs"
                subdir = os.path.join(bundle, sub)
                os.makedirs(subdir, exist_ok=True)
                copy_once(src, os.path.join(subdir, os.path.basename(path)))
                if sub == "docs":
                    docs.append(os.path.basename(path))
            else:
                print(f"  skip  unhandled role {role}: {path}")

    index = os.path.join(bundle, "index.md")
    if os.path.exists(index):
        print("index.md exists — left untouched")
        return

    lines = ["---",
             f'title: "{args.slug}"',
             'when:', '  - "TODO"',
             'what: "TODO"',
             'abstract: "TODO"']
    if hero:
        lines.append(f'heroImage: "./{hero}"')
    lines += ['tier: 1', 'draft: "true"', '---', '']
    lines += [f"{{{{< youtube {e} >}}}}" for e in embeds]
    lines.append("")
    lines.append("<!-- TODO: page body — pull prose from notes/ -->")
    lines.append("")
    lines += [f"![{args.slug}](./{g})" for g in gallery]
    lines.append("")
    lines += [f"[{d}](./docs/{d})" for d in docs]
    lines += [f"[{u}]({u})" for u in links]
    lines.append("")
    with open(index, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("scaffolded index.md")


if __name__ == "__main__":
    main()
