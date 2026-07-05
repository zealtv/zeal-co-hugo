#!/usr/bin/env python3
"""sweep — assisted collection pass for the publishing pipeline.

Walks source directories of raw project material and emits a markdown
manifest of publish candidates for human curation. Copies nothing.

    sweep.py <source-dir> [<source-dir>...] > manifest.md

Manifest lines are checkboxes with a guessed role:

    - [ ] hero     path/to/img.png  (1.2M)
    - [ ] gallery  path/to/img2.jpg (800K)
    - [ ] embed    path/to/clip.mp4 (1.9G)  # video: upload + embed, never git
    - [ ] doc      path/to/notes.md (4K)

Curate by deleting lines you reject and ticking lines you accept.
Deterministic: same input tree, same manifest. No network, no LLM.
"""

import os
import sys

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".tif", ".tiff"}
VIDEO_EXT = {".mp4", ".mov", ".mkv", ".avi", ".webm", ".m4v"}
AUDIO_EXT = {".wav", ".mp3", ".aif", ".aiff", ".flac", ".ogg", ".m4a"}
DOC_EXT = {".md", ".pdf", ".txt"}
HERO_HINTS = ("hero", "promo", "poster", "cover")

SKIP_DIRS = {"@eaDir", ".git", "node_modules", "__pycache__"}
SKIP_SUFFIXES = (".asd", ".af", ".blend", ".blend1", ".toe", ".als", ".pid")
SKIP_CONTAINS = ("~lock~",)


def human(n):
    for unit in ("B", "K", "M", "G", "T"):
        if n < 1024:
            return f"{n:.0f}{unit}"
        n /= 1024
    return f"{n:.0f}P"


def role_of(name):
    lower = name.lower()
    ext = os.path.splitext(lower)[1]
    if ext in IMAGE_EXT:
        return "hero" if any(h in lower for h in HERO_HINTS) else "gallery"
    if ext in VIDEO_EXT:
        return "embed"
    if ext in AUDIO_EXT:
        return "audio"
    if ext in DOC_EXT:
        return "doc"
    return None


def sweep(source):
    """Yield (relative-dir, [(role, relpath, size), ...]) groups, sorted."""
    groups = {}
    for dirpath, dirnames, filenames in os.walk(source):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        rel_dir = os.path.relpath(dirpath, source)
        for name in sorted(filenames):
            if name.startswith("."):
                continue
            lower = name.lower()
            if lower.endswith(SKIP_SUFFIXES) or any(s in lower for s in SKIP_CONTAINS):
                continue
            role = role_of(name)
            if role is None:
                continue
            full = os.path.join(dirpath, name)
            try:
                size = os.path.getsize(full)
            except OSError:
                continue
            groups.setdefault(rel_dir, []).append((role, os.path.relpath(full, source), size))
    return sorted(groups.items())


def main():
    sources = sys.argv[1:]
    if not sources:
        sys.exit(__doc__.strip())
    print("# sweep manifest")
    print()
    print("Curate: delete rejected lines, tick `[x]` accepted lines, correct roles.")
    for source in sources:
        source = os.path.abspath(source)
        print(f"\n## source: {source}\n")
        total = 0
        for rel_dir, entries in sweep(source):
            print(f"### {rel_dir}/  ({len(entries)} candidates)\n")
            for role, rel, size in entries:
                note = "  # video: upload + embed, never git" if role == "embed" else ""
                print(f"- [ ] {role:7s} {rel}  ({human(size)}){note}")
                total += 1
            print()
        print(f"_{total} candidates in {source}_")


if __name__ == "__main__":
    main()
