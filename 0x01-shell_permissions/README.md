# Learning Objectives
## Permissions
- What do the commands chmod, sudo, su, chown, chgrp do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user chown a file
- How to run a command with root privileges
- How to change user ID or become superuser
## Other Man Pages 
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid
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
| [0-iam_betty](./0-iam_betty) | Switche the current user to the user betty. |
| [1-who_am_i](./1-who_am_i) | Print the effective username of the current user. |
| [2-groups](./2-groups) | Print all the groups the current user is part of. |
| [3-new_owner](./3-new_owner) | Change the owner of the file hello to the user betty. |
| [4-empty](./4-empty) | Create an empty file called hello. |
| [5-execute](./5-execute) | Add execute permission to the owner of the file **hello**. |
| [6-multiple_permissions](./6-multiple_permissions) | Add execute permission to the owner and the group owner, and read permission to other users, to the file **hello**. |
| [7-everybody](./7-everybody) | Add execution permission to the owner, the group owner and the other users, to the file **hello**. |
| [8-James_Bond](./8-James_Bond) | Set the permission to the file **hello** as follows: Owner and Group have no permission at all, Other users have all the permissions. |
| [9-John_Doe](./9-John_Doe) | Set the mode of the file **hello** to **-rwxr-x-wx**. |
| [10-mirror_permissions](./10-mirror_permissions) | Set the mode of the file **hello** the same as **olleh**’s mode. |
| [11-directories_permissions](./11-directories_permissions) | Add execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. |
| [12-directory_permissions](./12-directory_permissions) | Create a directory called my_dir with permissions 751 in the working directory. |
| [13-change_group](./13-change_group) | Change the group owner to school for the file **hello**. |
| [100-change_owner_and_group](./100-change_owner_and_group) | Change the owner to vincent and the group owner to staff for all the files and directories in the working directory. |
| [101-symbolic_link_permissions](./101-symbolic_link_permissions) | Change the owner and the group owner of \_hello  to **vincent** and **staff** respectively. |
| [102-if_only](./102-if_only) | Change the owner of the file **hello** to **betty** only if it is owned by the user **guillaume**. |
| [103-Star_Wars](./103-Star_Wars) | Play the StarWars IV episode in the terminal. |
