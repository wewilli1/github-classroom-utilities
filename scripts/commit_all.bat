@echo off

rem %1: Commit message

python %pyscripts%\commit_all.py "%cd%" "%1"
