# Hello Hackers


  In this first module of Linux lunarium, The task was to execute commands on the terminal along with commands with arguments.

## Introduction To Commands
  


The description of this challenge states that invoking the `hello` command would give us the required flag.

In a previous example, `whoami` is   typed into the prompt and pressing enter prints `hacker` in the terminal screen.

Therefore typing `hello` and pressing the enter key retrieves flag `pwn.college{oERCrKzcHsev9cTG_t7xCMwdxE8.ddjNyUDLzQjN0czW}`

Note: Commands in linux are case sensitive.


## Introduction To Arguments

The description of this challenge gives us a brief description on what passing an argument is. 
Which is:
A command with arguments is what we call additional data passed to the command. When you type a line of text and hit enter, the shell actually parses your input into a command and its arguments. The first word is the command, and the subsequent words are arguments.

In a previous example, `echo hello` is input in the terminal which returns a `hello` as echo is a command that "echoes" all of it's arguments back into the terminal.

In a subsequent example, `echo hello hackers` is input to implement multiple arguments in the command `echo`.
As expected, we get `hello hackers` as the output.

Moving on to the challenge, I had to type the `hello` command (without the echo) with `hackers` as the argument and hit the enter key to get the flag :
`pwn.college{MEFLqur_IYn5P6YxTPZrf-pwQ0e.dhjNyUDLzQjN0czW}`