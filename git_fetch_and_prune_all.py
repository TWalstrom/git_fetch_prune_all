import os
import subprocess
import colorama
import sys

colorama.init(autoreset=True)

# Get parent directory from command line argument, or use current directory as default
parent_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
# usage: python script.py "C:\PATH\WHERE\REPOS\ARE\SAVED"

# Loop over all items in the parent directory
for dir in os.listdir(parent_dir):
    dir_path = os.path.join(parent_dir, dir)
    # If the item is a directory
    if os.path.isdir(dir_path):
        # Check if the directory is a Git repository
        if os.path.isdir(os.path.join(dir_path, ".git")):
            # Change into the directory
            os.chdir(dir_path)
            # Fetch from the remote repository and prune any branches that no longer exist on the remote
            subprocess.run(["git", "fetch", "origin", "--prune"])
        else:
            print(f"{dir_path} is not a Git repository, skipping...")
