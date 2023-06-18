# Learning Objectives
## Shell, I/O Redirection
- What do the commands **head**, **tail**, **find**, **wc**, **sort**, **uniq**, **grep**, **tr** do
- How to redirect standard output to a file
- How to get standard input from a file instead of the keyboard
- How to send the output from one program to the input of another program
- How to combine commands and filters with redirections
## Special Characters
- What are special characters
- Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
## Other Man Pages
- How to display a line of text
- How to concatenate files and print on the standard output
- How to reverse a string
- How to remove sections from each line of files
- What is the **/etc/passwd** file and what is its format
- What is the **/etc/shadow** file and what is its format
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
- You are not allowed to use **sed** or **awk**.
# Tasks
| Script | Description |
| ------ | ----------- |
| [0-hello_world](./0-hello_world) | Print “Hello, World”, followed by a new line to the standard output. |
| [1-confused_smiley](./1-confused_smiley) | Display a confused smiley "(Ôo)'. |
| [2-hellofile](./2-hellofile) | Display the content of the **/etc/passwd** file. |
| [3-twofiles](./3-twofiles) | Display the content of **/etc/passwd** and **/etc/hosts**. |
| [4-lastlines](./4-lastlines) | Display the last 10 lines of **/etc/passwd**. |
| [5-firstlines](./5-firstlines) | Display the first 10 lines of **/etc/passwd**. |
| [6-third_line](./6-third_line) | Display the third line of the file **iacta**. |
| [7-file](./7-file) | Create a file containing the text **Best School** ending by a new line. |
| [8-cwd_state](./8-cwd_state) | Write into the file **ls_cwd_content** the result of the command **ls -la**. |
| [9-duplicate_last_line](./9-duplicate_last_line) | Duplicate the last line of the file **iacta**. |
| [10-no_more_js](./10-no_more_js) | Delete all the regular files (not the directories) with a **.js** extension that are present in the current directory and all its subfolders. |
| [11-directories](./11-directories) | Count the number of directories and sub-directories in the current directory. |
| [12-newest_files](./12-newest_files) | Display the 10 newest files in the current directory. |
| [13-unique](./13-unique) | Take a list of words as input and prints only words that appear exactly once. |
| [14-findthatword](./14-findthatword) | Display lines containing the pattern “root” from the file **/etc/passwd**. |
| [15-countthatword](./15-countthatword) | Display the number of lines that contain the pattern “bin” in the file **/etc/passwd**. |
| [16-whatsnext](./16-whatsnext) | Display lines containing the pattern “root” and 3 lines after them in the file **/etc/passwd**. |
| [17-hidethisword](./17-hidethisword) | Display all the lines in the file **/etc/passwd** that do not contain the pattern “bin”. |
| [18-letteronly](./18-letteronly) | Display all lines of the file **/etc/ssh/sshd_config** starting with a letter. |
| [19-AZ](./19-AZ) | Replace all characters **A** and **c** from input to **Z** and **e** respectively. |
| [20-hiago](./20-hiago) | Create a script that removes all letters **c** and **C** from input. |
| [21-reverse](./21-reverse) | Reverse its input. |
| [22-users_and_homes](./22-users_and_homes) | Display all users and their home directories, sorted by users. Based on the **/etc/passwd** file. |
| [100-empty_casks](./100-empty_casks) | Find all empty files and directories in the current directory and all sub-directories. |
| [101-gifs](./101-gifs) | List all the files with a **.gif** extension in the current directory and all its sub-directories. |
| [102-acrostic](./102-acrostic) | Decode acrostics that use the first letter of each line. |
| [103-the_biggest_fan](./103-the_biggest_fan) | Parse web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests. |
