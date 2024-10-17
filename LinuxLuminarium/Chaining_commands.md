# Chaining Commands

This module is about chaining commands.


- [Chaining Commands](#chaining-commands)
  - [Chaining with Semicolons](#chaining-with-semicolons)
  - [Your First Shell Script](#your-first-shell-script)
  - [Redirecting Script Output](#redirecting-script-output)
  - [Executable Shell Scripts](#executable-shell-scripts)



## Chaining with Semicolons

In this challenge, we should chain the commands `/challenge/pwn` and `/challenge/college` in order to get the flag.

> [!NOTE]
> We can use `;` to chain commands in Linux.

I run **`/challenge/pwn; /challenge/college`** to get the flag.

```
hacker@chaining~chaining-with-semicolons:~$ /challenge/pwn ; /challenge/college
Yes! You chained /challenge/pwn and /challenge/college! Here is your flag:
pwn.college{k485ipG32ZWgWX2q-jT1KjiUrJ7.dVTN4QDLzQjN0czW}
hacker@chaining~chaining-with-semicolons:~$
```
The flag : `pwn.college{k485ipG32ZWgWX2q-jT1KjiUrJ7.dVTN4QDLzQjN0czW}`.


## Your First Shell Script

In this challenge, we should add our commands to a bash file called `x.sh` and run it in order to get our flag.

I use the command line text editor [nano](https://www.nano-editor.org/) to edit `x.sh` 


Finally I run `bash x.sh` to run the file and get the flag : 
`pwn.college{oz0sHJ-dUbH3eNEGG5Dij-GyMiF.dFzN4QDLzQjN0czW}`


## Redirecting Script Output

Similar to the previous challenge, we need to create a bash file and pipe the output of the script into `/challenge/solve`

I create a bash file called `x.sh` like the previous challenge using [nano](https://www.nano-editor.org/).

I run **`bash x.sh | /challenge/solve`** to pipe the output of the script into `/challenge/solve` to get the flag.

```
Connected!
hacker@chaining~redirecting-script-output:~$ nano x.sh
hacker@chaining~redirecting-script-output:~$ bash x.sh | /challenge/solve
Correct! Here is your flag:
pwn.college{whODnWXdlKgyOfdUPkOIDoyz2Y4.dhTM5QDLzQjN0czW}
hacker@chaining~redirecting-script-output:~$
```

THe flag : `pwn.college{whODnWXdlKgyOfdUPkOIDoyz2Y4.dhTM5QDLzQjN0czW}`


## Executable Shell Scripts

In this challenge, we are supposed to create a bash script that calls `/challenge/solve` and run it without explicitly invoking bash.

> [!NOTE]
> We can directly run a bash file without using the `bash` command by making the file executable

I create a bash file called `x.sh` like the previous challenge using [nano](https://www.nano-editor.org/).

Using the knowledge I gained in the previous challenges, I utilise the `chmod` command to make the file executable - **`chmod u+x x.sh`**

Finally I run **`./x.sh`** to get the flag.

```
hacker@chaining~executable-shell-scripts:~$ nano x.sh
hacker@chaining~executable-shell-scripts:~$ chmod u+x x.sh
hacker@chaining~executable-shell-scripts:~$ ./x.sh
Congratulations on your shell script execution! Your flag:
pwn.college{cGaIzWWD7tdhJ_ZEo8RQpzrkDkC.dRzNyUDLzQjN0czW}
hacker@chaining~executable-shell-scripts:~$
```

The flag : `pwn.college{cGaIzWWD7tdhJ_ZEo8RQpzrkDkC.dRzNyUDLzQjN0czW}`

# END