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
            
            # # find all content between double square brackets [[ content ]]
            # matches = re.findall(r"\[\[(.*?)\]\]", line)            
            # for match in matches:

            #     # filter only links pointing to files directory
            #     if "files/" in match:

            #         # truncate the path before the first occurrence of " ", "|", or ")", but only after a "." character
            #         match = truncated_string = re.match(r"^(.*?\.[^\ |\)]+)", match).group(1)
            #         file_links.append(match)


            # find all content between round brackets [ md link ]( content )
            matches = re.findall(r"\((.*?)\)", line)            
            for match in matches:

                # filter only links pointing to files directory
                if "files/" in match:

                    # truncate the path before the first occurrence of " ", "|", or ")", but only after a "." character
                    match = truncated_string = re.match(r"^(.*?\.[^\ |\)]+)", match).group(1)
                    file_links.append(match)



    # Return the list of file links
    return file_links



def process_wikilinks(markdown_file):
    # Read the entire contents of the markdown file into a string
    with open(markdown_file, "r") as f:
        contents = f.read()

    # # to test: Replace all "." characters with "?" characters
    # contents = contents.replace(".", "?")
    
    p = re.compile(r'!\[\[(.+?)\]\]')
    # contents = re.sub(p, r'![\1](../\1)', contents)
    contents = re.sub(p, r'![\1](../\1)', contents)
    
    # Write the modified contents back to the markdown file
    with open(markdown_file, "w") as f:
        f.write(contents)



def replace_youtube_links(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    youtube_link_regex = re.compile(r'\[.*\]\(https://youtube\.com/watch\?v=([^)\s]+)\)')
    content = youtube_link_regex.sub(r'{{< youtube \1 >}}', content)

    with open(file_path, 'w') as file:
        file.write(content)


def replace_vimeo_links(file_path):
    # Open the file and read its content
    with open(file_path, "r") as file:
        content = file.read()

    # Find all Vimeo links and replace them with Hugo shortcodes
    new_content = re.sub(r"\[.*\]\(https://vimeo.com/(\d+)\)", r"{{< vimeo \1 >}}", content)

    # Write the new content to the file
    with open(file_path, "w") as file:
        file.write(new_content)



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
                    print("Copying note: ", this_file)
                    
                    shutil.copy(src_full_path, dst_full_path)

                    process_wikilinks(dst_full_path)
                    replace_youtube_links(dst_full_path)
                    replace_vimeo_links(dst_full_path)
                    
                    
                    # !IMPORTANT! links to files (ie embeded images) must use relative paths
                    file_links = get_file_links(src_full_path)
                    
                    for file in file_links:
                        file = file.lstrip("../")
                        print("file: ", file)
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

dst_path = os.path.join(dst_path, "content")

# PROCESS NOTEBOOK

print("clearing content/notebook")
# Create the "notebook" directory in the destination path
notebook_dst_path = os.path.join(dst_path, "notebook")
shutil.rmtree(notebook_dst_path, ignore_errors=True)
os.makedirs(notebook_dst_path, exist_ok=True)

print("clearing content/files")
# Create "file" directory in the destination path
files_dst_path = os.path.join(dst_path, "files")
shutil.rmtree(files_dst_path, ignore_errors=True)
os.makedirs(files_dst_path, exist_ok=True)

print("processing obisdian notes")
# Iterate over src path and copy files
process_notebook(src_path, dst_path)



# TODO
# process in place MD files into hugo MD 
## convert image wikilinks to MD links
## convert link wikilinks to hugo refs: [About]({{< ref "/about" >}} "About Us")
## convert youtube links to hugo shortcodes
## convert vimeo links to hugo shortcodes

