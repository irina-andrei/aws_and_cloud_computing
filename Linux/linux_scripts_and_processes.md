# Linux Scripts and Processes

### Remember everything is CASE-SENSITIVE.

#### Some useful commands:
- Moving a file to a new location:
```
mv <file_name> <destination_folder>
```
- Getting extra file information (long hand):
```
ls -l 
```

<br>

## Scripts
- Creating and opening a Script file:
```
nano <script_name.sh>
```
- All comments you want to add to the script will start with '#'.
- A script needs to start with the character sequence `#!` (called *'shebang'*). This will tell the OS it's a script with commands that need to be run. 
- Example of a Script ('provision.sh'):

```
#!/bin/bash

# update
sudo apt update

# upgrade
sudo apt upgrade -y

# install nginx
sudo apt install nginx -y

# restart nginx
sudo systemctl restart nginx

# enable nginx
sudo systemctl enable nginx
```
- In this Script, it will update and upgrade the system, as well as install 'nginx' and start(or restart) it and by enabling it, 'nginx' will be added to Start Up.
- In order to run this Script, first you have to allow permision for it to be run (the '+x' will allow the file to be executable):
```
sudo chmod +x provision.sh
```
- Once it has permission, to run the Script you simply call it:
```
./provision.sh
```

<br>


## Processes

- Display the user proceses:
```
ps
```
-> PID : Process ID

-> CMD: Shows what command was used for that process

- Display the list of all process command options available: 
```
ps --help simple
```
- Display ALL processes: 
```
ps -A
```
- Display processes with more in-depth information: 
```
ps -aux
```
- Display a Live Read of all processes:
```
top
```
-> Shirt + 'M' : sorting by memory

-> Shirt + 'N' : sorting by newest process

-> Shirt + 'P' : sorting by CPU usage

-> 'Q' : exit


- Example of a dummy program that you can run in the foreground:
```
sleep 5
```
- If you want the program to run in the background, add `&` to your command (and this will also output a Process ID):
```
sleep 5000 &
```
- To pause a process:

```
Ctrl + 'Z'
```
- To terminate a process: 
```
kill -1 <process_ID>    # mild severity
kill -15 <process_ID>   # medium severity
kill -9 <process_ID>    # maximum severity
kill -KILL <process_ID>     # same level as '-9'
```

<br>

### Permissions

*Types of permissions*:
- Read Access (r, code number: 4)
- Write Access (w, code number: 2)
- Execute Access (x, code number: 1)

*Types of users*:
- Owner (u)
- Group permissions (g)
- Others (blank)

To change permissions:
```
sudo chmod xxx <file_name>
```

Examples of code changes:
- 777 gives permission to everyone.
- 400 only owner can read
- u+x
- -xw
- g-w


### Variables
- `printenv` will print all variables
- `printenv <variable_name>` will print the contents of the variable
- Variables can be *environmental* (entire OS has access) or *local* (only within the current process you have access, ex: BASH).
`export <variable_name>=<content>` will create an **environment variable**.