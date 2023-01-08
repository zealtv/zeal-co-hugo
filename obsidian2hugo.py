import os
import sys
import shutil

# Function to recursively iterate over all files in a directory
def iterate_files(src_path, dst_path):
    # Iterate over all files in the source path
    for name in os.listdir(src_path):
        # Get the full path of the file or directory
        src_full_path = os.path.join(src_path, name)
        # Get the corresponding path in the destination directory
        dst_full_path = os.path.join(dst_path, name)
        # If the file is a markdown file, copy it to the destination path
        if name.endswith(".md"):
            shutil.copy(src_full_path, dst_full_path)

# Get the path from the command line arguments
src_path = sys.argv[1]
dst_path = sys.argv[2]

# Create the "notebook" directory in the destination path
notebook_path = os.path.join(dst_path, "notebook")
shutil.rmtree(notebook_path, ignore_errors=True)
os.makedirs(notebook_path, exist_ok=True)

# Iterate over all files in the root of the source path
iterate_files(src_path, notebook_path)
