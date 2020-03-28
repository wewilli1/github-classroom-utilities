import os
import sys
import subprocess
from termcolor import colored

def list2str(command_list):
    return " ".join(command_list)

def get_user_name(repo_name, homework_name):
    user_name_index = repo_name.find(homework_name) + 1
    return repo_name[len(homework_name) + 1:]

def get_repo_list(repos_dir):
    # verify the top repo dir exists
    if not os.path.isdir(repos_dir):
        print("get_repo_list: Error, %s does not exist") % (repos_dir)
        sys.exit(1)

    # get a list of all student repos and files in the repos_dir
    repo_list = os.listdir(repos_dir)

    # define an empty list to store the student repos
    filtered_repo_list = []

    # for each file / dir in the repo_list
    for repo in repo_list:
        # build the full path repo name
        full_path_repo = "%s/%s" % (repos_dir, repo)
        if os.path.isdir(full_path_repo):
            filtered_repo_list.append(full_path_repo)

    # return the filtered repo list to the caller
    return filtered_repo_list

def git_command_single_repo(command_list, repo_dir):
    # change directory to the student's repo
    os.chdir(repo_dir)

    # perform the git command
    proc_status = subprocess.run(command_list, capture_output=True)

    # return the proc_status to the caller
    return proc_status

def git_command_all(command_list, repo_dir, silent=False):
    # get the list of student repos
    repo_list = get_repo_list(repo_dir)

    # create an empty list to hold repos where git pull failed
    error_list = []

    # create an empty list to hold command status objects
    proc_status_list = []

    # for each repo in the student repo list
    for repo_dir in repo_list:
        base_repo_name = os.path.basename(repo_dir)

        # if the silent flag is false
        if not silent:
            # print the repo and git command
            print(colored("Repo: %s" % (base_repo_name), 'blue'))
            print("Executing command: %s" % (list2str(command_list)))
            print(list2str(command_list))

        # execute the command on the repo
        proc_status = git_command_single_repo(command_list, repo_dir)

        # add the proc_status to the list
        proc_status_list.append((base_repo_name, proc_status))

        # print stdout
        if proc_status.stdout != None:
            print(proc_status.stdout.decode('utf-8'))

        # print stderr
        if proc_status.stderr != None:
            print(proc_status.stderr.decode('utf-8'))

        # if git returned an error code
        if proc_status.returncode != 0:
            error_list.append(base_repo_name)

    # if errors happened
    if len(error_list) > 0:
        print("Repos for which %s  failed:" % (list2str(command_list)))

        # for each repo in the error list
        for repo in error_list:
            print("  ", repo)

        print()
        print()

    # return the proc status list to the caller
    return proc_status_list
