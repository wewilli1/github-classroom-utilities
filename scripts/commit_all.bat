@echo off

rem %1: Repo directory
rem %2: Commit message

python "%classroom_utils%/python/commit_all.py" %1 %2
