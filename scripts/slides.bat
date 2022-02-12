@echo off
start jupyter nbconvert %1 --to slides --post serve
