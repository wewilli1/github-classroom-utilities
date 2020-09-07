@echo off

rem %1: Commit message

python "%classroom_utils%/python/commit_all.py" "%cd%" %1
