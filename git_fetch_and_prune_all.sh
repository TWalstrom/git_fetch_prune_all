#!/bin/bash

# Define the parent directory
parent_dir = "/PATH/TO/YOUR/REPOS/"

# Loop over all items in the parent directory
for dir in "$parent_dir"/*; do
    # If the item is a directory
    if [ -d "$dir" ]; then
        # Change into the directory
        cd "$dir" || continue
        # Check if the directory is a Git repository
        if [ -d ".git" ]; then
            # Fetch from the remote repository and prune any branches that no longer exist on the remote
            git fetch origin --prune
        else
            echo "$dir is not a Git repository, skipping..."
        fi
        # Change back to the parent directory before the next iteration
        cd "$parent_dir" || exit
    fi
done
# End of the for loop