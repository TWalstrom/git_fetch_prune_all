# README for `git_fetch_and_prune_all`

## What?
The `git_fetch_and_prune_all.sh` is a Bash script that automates the process of fetching and pruning all branches that no longer exist. If you have all your Git repositories in a specified parent directory it will loop through and fetch and prune all. `git_fetch_and_prune_all.py` behaves the same as the bash version (just another option!)


## Why?
I usually save all my Git Repositories in the same parent directory. Instead of manually fetching and pruning the Git repositries, I run this every morning or a few times a day.

## How?

The script works as follows:

1. It defines the parent directory. In this case, it's set to `/PATH/TO/ALL/YOUR/REPOS/HERE`.

2. It loops over all items in the parent directory.

3. For each item, it checks if it's a directory. If it's not, it skips to the next item.

4. If the item is a directory, it changes into that directory.

5. It then checks if the directory is a Git repository by looking for a `.git` directory.

6. If the directory is not a Git repository, it prints a message indicating this and skips to the next item.

7. If the directory is a Git repository, it fetches from the remote repository and prunes any branches that no longer exist on the remote.

8. After processing a directory, it changes back to the parent directory before the next iteration.

## Usage

Change the parent directory to where all your repos are saved.

To use this script, you need to have Git installed on your machine. You can check this by doing a `git --version`.

You can run the script from the terminal by navigating to the directory containing the git_fetch_and_prune_all.sh and run it by typing `./git_fetch_and_prune_all.sh`

