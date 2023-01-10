import os
import re
import sys
import shutil
import frontmatter


def has_publish_frontmatter(markdown_file):
    with open(markdown_file, "r") as f:

        thismdfile = frontmatter.load(f)

        if 'publish' in thismdfile and thismdfile['publish'] == 'y':
            return True

    # Return False if the frontmatter does not contain the "publish" property or if it is not set to True
    return False


def get_file_links(markdown_file):
    # Initialize a list to store the file links
    file_links = []
    # Open the markdown file for reading
    with open(markdown_file, "r") as f:
        # Iterate over all lines in the file
        for line in f:
            
            # find all content between double square brackets [[ content ]]
            matches = re.findall(r"\[\[(.*?)\]\]", line)            

            for match in matches:

                # filter only links pointing to files directory
                if "files/" in match:

                    # truncate the path before the first occurrence of " ", "|", or ")", but only after a "." character
                    match = truncated_string = re.match(r"^(.*?\.[^\ |\)]+)", match).group(1)
                    file_links.append(match)

    # Return the list of file links
    return file_links



def process_notebook(src_path, dst_path):

        src_notebook_path = os.path.join(src_path, "notebook")

        # Iterate over all files in the source path
        for this_file in os.listdir(src_notebook_path):
            
            # Create source and destination paths of 
            src_full_path = os.path.join(src_path, "notebook", this_file)
            dst_full_path = os.path.join(dst_path, "notebook", this_file)

            if this_file.endswith(".md"):
                # Check if markdown file has publish flag
                doPublish = False
                try:
                    doPublish = has_publish_frontmatter(src_full_path)
                except:
                    print("!!! Broken front matter: ", this_file, "!!!")

                if doPublish:
                    print("Found markdown to publish: ", this_file)
                    
                    shutil.copy(src_full_path, dst_full_path)
                    
                    # !IMPORTANT! links to files (ie embeded images) must use relative paths
                    file_links = get_file_links(src_full_path)
                    
                    for file in file_links:

                        file_src_full_path = os.path.join(src_path, file)
                        file_dst_full_path = os.path.join(dst_path, file)

                        if os.path.isfile(file_src_full_path):
                            print("Copying file: ", file_src_full_path)
                            shutil.copy(file_src_full_path, file_dst_full_path)
                        else:
                            print("!!! File not found. Skipping: ", file_src_full_path, " !!!")





# MAIN ----------------------------------------------------
# Get the path from the command line arguments
src_path = sys.argv[1]
dst_path = sys.argv[2]


# PROCESS NOTEBOOK

# Create the "notebook" directory in the destination path
notebook_dst_path = os.path.join(dst_path, "notebook")
shutil.rmtree(notebook_dst_path, ignore_errors=True)
os.makedirs(notebook_dst_path, exist_ok=True)

# Create "file" directory in the destination path
files_dst_path = os.path.join(dst_path, "files")
shutil.rmtree(files_dst_path, ignore_errors=True)
os.makedirs(files_dst_path, exist_ok=True)


# Iterate over src path and copy files
process_notebook(src_path, dst_path)


# TODO 
# Process notebook, projects, literature notes etc independantly


# TODO
# process in place MD files into hugo MD 
## convert wikilinks to MD links
## convert youtube links to hugo shortcodes
## convert vimeo links to hugo shortcodes

