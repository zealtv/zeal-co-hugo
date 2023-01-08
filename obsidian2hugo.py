import os
import sys
import shutil
import frontmatter

# Function to check if markdown file is has publish=True in yaml frontmatter
def has_publish_frontmatter(markdown_file):
    with open(markdown_file, "r") as f:

        thismdfile = frontmatter.load(f)

        if 'publish' in thismdfile and thismdfile['publish'] == 'y':
            return True

    # Return False if the frontmatter does not contain the "publish" property or if it is not set to True
    return False


# Function to recursively iterate over all files in a directory
def iterate_files(src_path, dst_path):
    # Iterate over all files in the source path
    for name in os.listdir(src_path):

        # TODO for project files, check markdown file for publish=y
        # copy entire folders for project including assets etc

        # If the file is a markdown file, copy it to the destination path
        if name.endswith(".md"):
            # Get the full path of the file or directory
            src_full_path = os.path.join(src_path, name)

            # Check if markdown file has publish flag
            if has_publish_frontmatter(src_full_path):
                # Get the corresponding path in the destination directory
                dst_full_path = os.path.join(dst_path, name)
                shutil.copy(src_full_path, dst_full_path)



# MAIN ----------------------------------------------------
# Get the path from the command line arguments
src_path = sys.argv[1]
dst_path = sys.argv[2]

# Create the "notebook" directory in the destination path
notebook_path = os.path.join(dst_path, "notebook")
shutil.rmtree(notebook_path, ignore_errors=True)
os.makedirs(notebook_path, exist_ok=True)

# Iterate over all files in the root of the source path
iterate_files(src_path, notebook_path)

# TODO
# process copied markdown files in place into hugo MD
