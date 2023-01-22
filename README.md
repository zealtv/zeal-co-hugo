# ZEAL.CO

This website is built with Hugo. Hugo is less of a mess than Gatsby but Go is wierd. I have secret plans this for website - plans that are unknown even to myself.

The content of this website is pulled from my private obsidian vault and may include project documentation, research and development notes, literature notes, and various other markdown anomolies.  

It pulls from an obsidian notebook, parsing files with a publish: y frontmatter tag for hugo.  This is done with the python script [./obsidian2hugo.py](./obsidian2hugo.py)

## Python Script Requires:

```
pip install python-frontmatter
```

## Updating Content

to build content/notebook and content/files, run:

```
./obsidian2hugo.py [obsidian-notebook path] [zeal-co-hugo path]

# ie
./obsidian2hugo.py ../notebook ./
``` 

Then commit and push to git to send live.  

Commands can be tied to a hotkey from within obsidian using the *shell commands* plugin.