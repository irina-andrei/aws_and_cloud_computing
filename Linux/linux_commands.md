# Linux Commands

### BASH (Born Again Shell)
#### -> Interface that allows to **run commands**.
#### -> It's considered the *default shell*.
#### -> Some useful commands:

<br>

- Printing the processor specifications:

```
uname -p
```

- Finding the current username:
```
whoami
```

<br>

### Directory related commands:
- Display folders/files in higher directory:
```
ls ..
```

- Display folders/files in current directory:
```
ls 
```

- Outputting current directory location:
```
pwd
```

- Outputting the valid login shells:
```
cat /etc/shells
```

- Moving location to ROOT:
```
cd /
```
- Moving location to HOME:
```
cd
```

<br>

### Commands History

- Showing commands history:
```
history
```

- Clearing all commands history:
```
history -c
```


<br>

### Files Management

- Transferring data from a link:
```
curl <link> --output <name_of_new_file>
```

- Outputting the contents of a file:
```
cat <file>
```

- Displaying the file data type:
```
file <name>
```

- Renaming a file:
```
mv <name_of_file> <new_name>
```

- Copying a file:
```
cp <file_to_copy> <new_copy_name>
```

- Deleting a file:
```
rm <file>
```

- Creating a new file that will be blank:
```
touch <new_blank_file>
```

<br>

### Directory Management

- Deleting a directory (first one to try):
```
rm -r <name_to_delete> 
```

- Deleting a directory with *force* (if **-r** doesn't work):
```
rm -rf <name_to_delete> 
```

- Creating a new directory (folder):
```
mkdir <new_directory_name>
```

<br>

### Text Editor and Text Files

- Opening the in-built Text Editor (use Ctrl + "..." to control):
```
nano <file_name.txt>
```

- Printing out the first n lines of a file:
```
head -n <file_name>
```

- Printing out the last n lines of a file:
```
tail -n <file_name>
```

- Printing all lines that aren't blank with numbered bullet points:
```
nl <file_name>
```

- Showing all lines with occurences of a specific word inside a file:
```
cat <file_name> | grep <something_to_search>
```

<br>

### Super User

- Install something as a temporary Super User (without `sudo` command, this won't work):
```
sudo apt install <program>
```

- Becoming a permanent Super User (root):
```
sudo su
```

- Exiting 'Super User' and reverting to original user login:
```
exit
```

<br>

### Logging Out

- Logging out of the server:
```
logout
```