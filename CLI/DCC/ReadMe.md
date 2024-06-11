## `dcc.py` version 1.1 `last checked 29 Jul 2022`

Daily Coding Problem

## What this script does:

[**Windows only**]
This script creates a new folder for every day based on system time and pushes it to github.

## What is the best way to use it [in my opinion]:

It already creates `Problem for {today}.txt` which can be a coding problem to be done everyday.

## What this script could do [work in progress]:

Retrive problems from the web and give a problem everyday, as well as an option to get a solution if need be.

## How to use it:

First we set a directory path as the location where we cloned our GitHub Repository. This script, on running, checks a date and creates a new folder for the set year, month and date and then in it a notepad file called `problem`. It can be used with [Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) to create a new folder everyday at a set time. Then we must set up git bash for that directory if there isnt one in the 'root' github directory (Usually: `C:/Users/Documents/Github`). Once that is done, this script can commit and push the folder straight to github.

# Notes:

Must change the path in `DCC.py` and clone your GitHub Repo where you would be storing the code in the path.

# Known bugs:

> -Why is it called 'dcc.py'?
> -DCC stands for Daily Coding Problem, an acronym for [DailyCodingProblem](dailycodingproblem.com) which I used a lot and wanted to have a way to solve the daily problem everyday and push it to github so that I could use github UI to track how many problems I have done based on number of pushes to the repository, However I have yet to implement a way to get the problem from dailycodingproblem.com .

---
