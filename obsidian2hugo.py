import os
import re
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


#TODO should do this for both wikistyle and markdown style files
def get_file_links(markdown_file):
    # Initialize a list to store the file links
    file_links = []
    # Open the markdown file for reading
    with open(markdown_file, "r") as f:
        # Iterate over all lines in the file
        for line in f:
            # Use a regular expression to find links to files in the "/files" directory
            match = re.search(r"\[.*\]\((files/.*)\)", line)
            # If a match was found, add the link to the list
            if match:
                file_links.append(match.group(1))
    # Return the list of file links
    return file_links



# Function to recursively iterate over all files in a directory
def iterate_files(src_path, dst_path):

        # Iterate over all files in the source path
        for name in os.listdir(src_path):
            
            # Get the full path of the file or directory
            src_full_path = os.path.join(src_path, name)
            dst_full_path = os.path.join(dst_path, name)


            is_hidden = os.path.split(name)[1].startswith(".")

            if os.path.isdir(src_full_path) and not is_hidden and name != "files":
                print("processing folder: ", src_full_path)
                # print(dst_full_path)
                #recursively iterate files
                iterate_files(src_full_path, dst_full_path)


            # process markdown files
            # look for linked assets
            # handle projects separately

            #----- PROJECT NOTES AND FOLDERS
            # TODO for project files, check markdown file for publish=y
            # copy entire folders for project including assets etc

            

            #----- NOTES IN ROOT OF VAULT
            # If the file is a markdown file in the root of the vault, copy it to the notebook folder
            
            # TODO for ease of linking we probably want to keep the structure of the content folder and obsidian vault the same.
            # ie put notebook notes in notebook.
            # notes in root become pages (if publish flag is present)

            if name.endswith(".md"):
                # Check if markdown file has publish flag

                try:
                    doPublish = has_publish_frontmatter(src_full_path)
                except:
                    print("Broken front matter: ", name)

                if doPublish:
                    print("found markdown to publish: ", name)
                    # Get the corresponding path in the destination directory
                    
                    # dst_full_path = os.path.join(notebook_path, name)
                    shutil.copy(src_full_path, dst_full_path)
                    
                    # TODO copy files linked in any published markdown documents  
                    # !IMPORTANT! links to files (ie embeded images) must use relative paths
                    file_links = get_file_links(src_full_path)
                    
                    for file in file_links:
                        print("Found file linked in markdown: ", file)

                        file_src_full_path = os.path.join(src_path, file)
                        file_dst_full_path = os.path.join(dst_path, file)
                        if os.path.isfile(file_src_full_path):
                            print("Copying file: ", file_src_full_path)
                            shutil.copy(file_src_full_path, file_dst_full_path)
                        else:
                            print("File not found. Skipping: ", file_src_full_path)



# MAIN ----------------------------------------------------
# Get the path from the command line arguments
src_path = sys.argv[1]
dst_path = sys.argv[2]



# Create destination folders

# Create the "notebook" directory in the destination path
notebook_dst_path = os.path.join(dst_path, "notebook")
shutil.rmtree(notebook_dst_path, ignore_errors=True)
os.makedirs(notebook_dst_path, exist_ok=True)

# Create "file" directory in the destination path
files_dst_path = os.path.join(dst_path, "files")
shutil.rmtree(files_dst_path, ignore_errors=True)
os.makedirs(files_dst_path, exist_ok=True)


# TODO 
# Process notebook, projects, literature notes etc independantly

# Iterate over src path and copy files
iterate_files(src_path, dst_path)


# TODO
# process in place MD files into hugo MD 
## convert wikilinks to MD links
## convert youtube links to hugo shortcodes
## convert vimeo links to hugo shortcodes
