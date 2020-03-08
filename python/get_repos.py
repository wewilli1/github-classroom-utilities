# this script is experimental and under development

import github3

gh = github3.Github()
all_repos = gh.repos.list(user="https://classroom.github.com/classrooms/55932271-ist-718-spring-2020-tuesday/assignments/ist-718-spring-2020-homework-2").all()

print(all_repos)
