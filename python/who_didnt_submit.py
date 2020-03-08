from github_classroom_utils import git_command_all
from github_classroom_utils import get_user_name
import os
import sys

# define the expected number of args
expected_num_args = 3

# define the argument indices
repo_name_index = 0
repo_dir_index = 1
homework_name_index = 2

# get the args
repo_dir = sys.argv[repo_dir_index]
homework_name = sys.argv[homework_name_index]

# if the received num of args not equal to expected num args
if len(sys.argv) != expected_num_args:
    print("Usage: %s <student_repo_dir> <homework_name>" % sys.argv[0])
    print("  Example:")
    print("  %s c:/repos/tuesday ist-718-spring-2020-homework-1")
    sys.exit(1)

proc_status_list = git_command_all(['git', 'log', '-1'], sys.argv[repo_dir_index],
                                   True)

# define the proc_status object index
proc_status_index = 1

# for each tuple in the list
for proc_status_tuple in proc_status_list:
    # extract the repo name from the tuple
    repo_name = proc_status_tuple[repo_name_index]

    if proc_status_tuple[proc_status_index].stdout != None:
        # convert the stdout bytes to a string
        stdout_str = proc_status_tuple[proc_status_index].stdout.decode('utf-8')

        # extract the git user name from the student repo name
        user_name = get_user_name(repo_name, homework_name)

        # if the user name is not in the last commit message
        if stdout_str.find(user_name) == -1:
            # This student did not make any commits
            print(user_name)
