# Learning Objectives
## General
- What does RTFM mean?
- What is a Shebang
## What is the Shell
- What is the shell
- What is the difference between a terminal and a shell
- What is the shell prompt
- How to use the history (the basics)
## Navigation
- What do the commands or built-ins **cd**, **pwd**, **ls** do
- How to navigate the filesystem
- What are the . and .. directories
- What is the working directory, how to print it and how to change it
- What is the root directory
- What is the home directory, and how to go there
- What is the difference between the root directory and the home directory of the user root
- What are the characteristics of hidden files and how to list them
- What does the command **cd -** do
## Looking Around
- What do the commands **ls**, **less**, **file** do
- How do you use options and arguments with commands
- Understand the ls long format and how to display it
- [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
- What does the **ln** command do
- What do you find in the most common/important directories
- What is a symbolic link
- What is a hard link
- What is the difference between a hard link and a symbolic link
## Manipulating Files
- What do the commands **cp**, **mv**, **rm**, **mkdir** do
- What are wildcards and how do they work
- How to use wildcards
## Working with Commands
- What do **type**, **which**, **help**, **man** commands do
- What are the different kinds of commands
- What is an alias
- When do you use the command help instead of man
## Reading Man Pages
- How to read a man page
- What are man page sections
- What are the section numbers for User commands, System calls and Library functions
## Keyboard Shortcuts for Bash
- Common shortcuts for Bash
## LTS
- What does **LTS** mean?
# Requirements
- Allowed editors: **vi**, **vim**, **emacs**
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (**$ wc -l file** should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly **#!/bin/bash**
- A **README.md** file at the root of the repo, containing a description of the repository
- A **README.md** file, at the root of the folder of this project, describing what each script is doing
- You are not allowed to use backticks, **&&**, **||** or **;**
- All your scripts must be executable. To make your file executable, use the **chmod** command: **chmod u+x file**. Later, we’ll learn more about how to utilize this command.
# Tasks
| Script | Description |
| ------ | ----------- |
| [0-current_working_directory](./0-current_working_directory) | Print the absolute path name of the current working directory. |
| [1-listit](./1-listit) | Display the contents list of your current directory. |
| [2-bring_me_home](./2-bring_me_home) | Change the working directory to the user’s home directory |
| [3-listfiles](./3-listfiles) | Display current directory contents in a long format. |
| [4-listmorefiles](./4-listmorefiles) | Display current directory contents, including hidden files. Long format. |
| [5-listfilesdigitonly](./5-listfilesdigitonly) | Display current directory contents. Long format, user and group ID numerically and hidden files. |
| [6-firstdirectory](./6-firstdirectory) | A script that creates a directory named **my_first_directory** in the **/tmp/** directory. |
| [7-movethatfile](./7-movethatfile) | Move the file **betty** from **/tmp/** to **/tmp/my_first_directory**. |
| [8-firstdelete](./8-firstdelete) | Delete the file **betty** in **/tmp/my_first_directory**. |
| [9-firstdirdeletion](./9-firstdirdeletion) | Delete the directory **my_first_directory** that is in the **/tmp** directory. |
| [10-back](./10-back) | Changes the working directory to the previous one. |
| [11-lists](./11-lists) | List all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the **/boot** directory (in this order), in long format. |
| [12-file_type](./12-file_type) | Print the type of the file named **iamafile**. The file **iamafile** is in the **/tmp** directory. |
| [13-symbolic_link](./13-symbolic_link) | Create a symbolic link to **/bin/ls**in the working directory, named **__ls__** |
| [14-copy_html](./14-copy_html) | Copie all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. |
| [100-lets_move](./100-lets_move) | Move all files beginning with an uppercase letter to the directory **/tmp/u**. **/tmp/u** already exists. |
| [101-clean_emacs](./101-clean_emacs) | Delete all files in the current working directory that end with the character **~**. |
| [102-tree](./102-tree) | Create the directories **welcome/**, **welcome/to/** and **welcome/to/school** in the current directory. Using two spaces (and lines) in the script. |
| [103-commas](./103-commas) | List all the files and directories of the current directory, separated by commas (**,**). |
| [school.mgc](./school.mgc) | Magic file that can be used with the command **file** to detect **School** data files. **School** data files always contain the string **SCHOOL** at offset 0. |
