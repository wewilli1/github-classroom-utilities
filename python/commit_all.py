from github_classroom_utils import git_command_all
import os
import sys

# define the expected number of args
expected_num_args = 3

# define the arg indices
repo_index = 1
msg_index = 2

# get the args
repo_dir = sys.argv[repo_index]
msg = sys.argv[msg_index]

# if the received num of args not equal to expected num args
if len(sys.argv) != expected_num_args:
    print("Usage: %s <student_repo_dir>" % sys.argv[0])
    sys.exit(1)

git_command_all(['git', 'commit', "-a", "-m", msg], sys.argv[1])
