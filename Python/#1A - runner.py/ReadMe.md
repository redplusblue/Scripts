# `runner.py` version 1.0 last checked 29 Jul 2022

## What this script does (default): 
This script(runner.py file) on being opened, opens the pdf file test.pdf which we have to set to be [opened by edge](https://helpdeskgeek.com/how-to/how-to-change-the-default-program-to-open-a-file-with/) and then reads the pdf aloud using edge's read aloud feature.  

## What this script can do [Extended use]:
1. Can be used to open any weblink (eg youtube) or any other program instead of a .pdf file. 
2. Other keyboard keys can be emulated with other programs, for instance: It can open a new chrome window and press `ctrl + h` to open `chrome://history`

## What is the best way to use it [in my opinion]:
Use windows [Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) in combination with the script, if youre on windows 

# Notes: 
1. Keep delay between key up and key down to avoid simultaneous press / prevent erroneous behaviour 

# Known bugs: 
1. A time delay between the opening of edge and execution of keyboard commands may result in the pdf not being read aloud properly. Can be fixed by adjusting according to opening times or pressing the key combination repeatedly. 

> -Why is it called 'runner.py'? 
> -Being my first script ever, I wanted to name it in a way that its function would be obvious, so I called it 'runner' because it *ran*, make of it what you will.
----------------------------------------------------------------------------


Samir K
