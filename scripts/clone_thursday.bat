@echo off

rem if the user did not pass the one required arg
if "%~1"=="" (
   rem echo a help message and bail out
   echo %~n0 homework_repo_name
   echo example: %~n0 ist-718-fall-2020-homework-1
   exit /B 1
)

rem clone the repos
python "%classroom_utils%/python/CloneAssignment.py" "IST-718-fall-2020" %1 "%repos%/student_repos/students_thursday.txt"
