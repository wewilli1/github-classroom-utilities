from github_classroom_utils import git_command_all
import os
import sys

# define the expected number of args
expected_num_args = 2

# define the argument indices
repo_dir_index = 1

# get the arg
repo_dir = sys.argv[repo_dir_index]

# if the received num of args not equal to expected num args
if len(sys.argv) != expected_num_args:
    print("Usage: %s <student_repo_dir>" % os.path.basename(sys.argv[0]))
    sys.exit(1)

git_command_all(['git', 'pull'], sys.argv[repo_dir_index])
