# Pondering PATH

This module is about the PATH variable in Linux.



- [Pondering PATH](#pondering-path)
  - [The PATH Variable](#the-path-variable)
  - [Setting PATH](#setting-path)
  - [Adding Commands](#adding-commands)
  - [Hijacking Commands](#hijacking-commands)


## The PATH Variable

In this challenge, we are supposed to make it so that `/challenge/run` cannot use the `rm` command in order to get our flag.

> [!NOTE]
> The shell will search for programs corresponding to commands in a special variable called the `PATH` variable.

We can set the value of the `PATH` variable to an empty string to prevent the program from accessing the `rm` command. The program 
`/challenge/run` will be a child process of our shell so we can export the `PATH` variable since child processes inherit the variables of the parent shell

I run **`export PATH=""`** to export the `PATH` variable as a empty string.

Then I run **`/challenge/run`** to get the flag.

```
Connected!
hacker@path~the-path-variable:~$ export PATH=""
hacker@path~the-path-variable:~$ /challenge/run
Trying to remove /flag...
/challenge/run: line 4: rm: No such file or directory
The flag is still there! I might as well give it to you!
pwn.college{oHPGAGCRKjUPAjH5JVMsy1TFQD3.dZzNwUDLzQjN0czW}
hacker@path~the-path-variable:~$
```
The flag : `pwn.college{oHPGAGCRKjUPAjH5JVMsy1TFQD3.dZzNwUDLzQjN0czW}`


## Setting PATH

In this challenge, the program `/challenge/run` will run the win command via its bare name, but this command exists in the `/challenge/more_commands/` directory, which is not initially in the `PATH` variable. Therefore we need to add the path to the `PATH` variable to get our flag.

I run **`PATH=/challenge/more_commands/`** to set the path variable.

Then I run **`/challenge/run`** to get the flag.

```
Connected!
hacker@path~setting-path:~$ PATH=/challenge/more_commands/
hacker@path~setting-path:~$ /challenge/run
Invoking 'win'....
Congratulations! You properly set the flag and 'win' has launched!
pwn.college{wxicxqMKVCx8td6j7j-eYd9XJPx.dVzNyUDLzQjN0czW}
hacker@path~setting-path:~$

```
The flag : `pwn.college{wxicxqMKVCx8td6j7j-eYd9XJPx.dVzNyUDLzQjN0czW}`


## Adding Commands

In this challenge, we need to trick `/challenge/run` into printing the flag by modifying the `win` file. 

I used [nano](https://www.nano-editor.org/) to create a file named `win` in the home directory:

> [!NOTE]
> Since we are modifying the `PATH` variable, the system can't find comamnds like `cat`. Therefore we have to use alternative methods to print out the flag.
>
> One such method is the `read` command which reads the contents of a file into a variable. We can then print out the variable using `echo`
>

I made it executabe for all users by running **`chmod o+x win`**

Then I modify the PATH variable - `PATH=~/`

Finally I run **`/challenge/run`** to get the flag -
