# ZEAL.CO

This website is built with Hugo. Hugo is less of a mess than Gatsby but Go is wierd. I have secret plans this for website - plans that are unknown even to myself.

The content of this website is pulled from my private obsidian vault includes project documentation, research and development notes, literature notes, and pieces of writing.  The vault is iterated over and parsed in to hugo formatted markdown by way of a python script, and copied into the content folder of this repository. In this way the website is a public facing version of ZEAL CO creative output and research.

## Python Script Requires:

```
pip install python-frontmatter
```

## Updating Content
to build content/notebook and content/files, run:

```
./obsidian2hugo.py [obsidian notebook path] [zeal-co-hugo path]

# ie
./obsidian2hugo.py ../notebook ./
``` 

Then commit and push to git.  This can all be tied to a hotkey from within obsidian using the *shell commands* plugin.