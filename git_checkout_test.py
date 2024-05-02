import os
import subprocess

# Define the parent directory
parent_dir = r"C:\Users\trawals\source\repos\RWSC Projects"

# Loop over all items in the parent directory
for dir in os.listdir(parent_dir):
    dir_path = os.path.join(parent_dir, dir)
    # If the item is a directory
    if os.path.isdir(dir_path):
        # Check if the directory is a Git repository
        if os.path.isdir(os.path.join(dir_path, ".git")):
            # Change into the directory
            os.chdir(dir_path)
            # Run the 'git checkout test' command
            subprocess.run(["git", "checkout", "test"], check=True)
        else:
            print(f"{dir_path} is not a Git repository, skipping...")