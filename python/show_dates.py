from github_classroom_utils import git_command_all
import os
import sys
import datetime as dt
import numpy as np

# define the expected number of args
expected_num_args = 3

# if the received num of args not equal to expected num args
if len(sys.argv) != expected_num_args:
    print("Usage: %s <student_repo_dir> <due_date>" % os.path.basename(sys.argv[0]))
    print("  Due Date Example for March 26 2020 11:59 PM: 2020-03-26 23:59:59 -0400")
    sys.exit(1)

# define the argument indices
repo_dir_index = 1
due_date_index = 2

# get the arg
repo_dir = sys.argv[repo_dir_index]
due_date_str = sys.argv[due_date_index]

# define the date time format str
date_format_str = "%Y-%m-%d %H:%M:%S %z"

# convert the due date string to a datetime object
due_date = dt.datetime.strptime(due_date_str, date_format_str)

# get the date of the last commit for all student repos
proc_stat_list = git_command_all(['git', 'log', '-1', '--format=%cd', '--date=iso'], sys.argv[repo_dir_index])

# define the num seconds per day
seconds_per_day = 60 * 60 * 24

# for each git log result
for proc_stat in proc_stat_list:
    # get the student repo
    repo = proc_stat[0]

    # create a date object from the result
    date_str = str(proc_stat[1].stdout.decode("utf-8")).strip()

    # get the day, month, day of month, hh:mm:ss yyyy
    commit_date = dt.datetime.strptime(date_str, date_format_str)

    if commit_date > due_date:
        # compute the number of days late
        delta = commit_date - due_date

        # compute the number of seconds late
        seconds_late = (delta.days * seconds_per_day) + delta.seconds

        # compute the number of days late
        days_late = np.ceil(seconds_late / seconds_per_day)

        print(repo, days_late, "days")
