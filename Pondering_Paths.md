# PONDERING PATHS

The Linux filesystem is a "tree". That is, it has a root (written as `/`). The root of the filesystem is a directory, and every directory can contain other directories and files.

 You refer to files and directories by their path. A path from the root of the filesystem starts with `/`(that is, the root of the filesystem), and describes the set of directories that must be descended into to find the file. 
 
 Every piece of the path is demarcated with another `/`.


This module of Linux Lunarium is all about file paths.
## <u><b><i>Challenges</i></b></u>


### <u>The Root</u>

In this challenge, We learn how to access/invoke a file using this path.

Therefore, to get invoke the file we give the exact path starting with `/` and this path is called the `absolute path`.


In the challenge, I retrieved the flag by invoking the program `pwn` by using the absolute path `/pwn`.

The flag : `pwn.college{k5LpEAPJNeoPTgw24o97af1q5_x.dhzN5QDLzQjN0czW}`



### <u><b><i>Program And Absolute Path </u></i></b>

In this challenge, we learn that all challenges are in the `challenge` directory and the `challenge` directory itself is in the `/` directory.

The name of the challenge program in this level is `run`, and it is in the `/challenge` directory. Thus, the path to the run challenge program is `/challenge/run`, therefore after we ssh and type the command in the terminal, we get the flag:

`pwn.college{8Ke7XwuxTSIhovtpbQpkCA6z-Y7.dVDN1QDLzQjN0czW}`

### <u><b><i>Position Thy Self</u></b></i>

In this challenge, we learn the command `cd` which can help us navigate between directories by passing a path to it as an argument like this : `cd /some/new/directory`.

In the given challenge, the run program was in a path I did not know about.

Thus I tried entering `/challenge/run` in the default directory which give this prompt :

Incorrect...

You are not currently in the `/usr/include` directory.

Then I used the aforementioned `cd` command to navigate to the the directory by typing `cd /usr/include` in the terminal
which then switched the directory to the desired one and then after typing `/challenge/run`, I retrieved the flag :

`pwn.college{UwbN4ANHTwaZ417PYkOTF2Y_GHx.dZDN1QDLzQjN0czW}`

### <u><b><i>Position Elsewhere</u></b></i>

Note: Basically the thought process is same as position thy self

In this challenge, we learn to implement the command `cd` which can help us navigate between directories by passing a path to it as an argument like this : `cd /some/new/directory`.

In the given challenge, the run program was in a path I did not know about.
Thus I tried entering `/challenge/run` in the default directory which give this prompt :

Incorrect...

You are not currently in the `/usr/share/zoneinfo/posix/Asia` directory.

Then I used the aforementioned `cd` command to navigate to the the directory by typing `cd /usr/share/zoneinfo/posix/Asia` in the terminal which then switched the directory to the desired one and then after typing `/challenge/run`, I retrieved the flag :

`pwn.college{A_gDEB1ShL8wiQx7ADEmfw8GZ0Y.ddDN1QDLzQjN0czW}`

### <u><b><i>Position Yet elsewhere</u></b></i>

Note: Basically the thought process is same as position thy self

In this challenge, we agian learn to implement the command `cd` which can help us navigate between directories by passing a path to it as an argument like this : `cd /some/new/directory`.

In the given challenge, the run program was in a path I did not know about.
Thus I tried entering `/challenge/run` in the default directory which give this prompt :

Incorrect...

You are not currently in the `/usr/share/zoneinfo/posix/Asia` directory.


Then I used the aforementioned `cd` command to navigate to the the directory by typing `cd /usr/share/zoneinfo/posix/Asia` in the terminal which then switched the directory to the desired one and then after typing `/challenge/run`,

 I retrieved the flag :


`pwn.college{8jQH6Gply6QpexzIzpWB6x_gG-G.dhDN1QDLzQjN0czW}`



### <u><b><i>Implicit Relative paths from /</u></b></i>

In this challenge, we learn about relative paths :

*A relative path is any path that does not start at root (i.e., it does not start with `/`).

*A relative path is interpreted relative to your current working directory (cwd).

*Your cwd is the directory that your prompt is currently located at.



This means how you specify a particular file, depends on where the terminal prompt is located.

Imagine we want to access some file located at /tmp/a/b/my_file.

If my cwd is `/`, then a relative path to the file is tmp/a/b/my_file.

If my cwd is `/tmp`, then a relative path to the file is a/b/my_file.

If my cwd is `/tmp/a/b/c`, then a relative path to the file is ../my_file. The .. refers to the parent directory.



To solve this challenge, 

I accessed the root directory `/` using  `cd /` and then  invoked the command `challenge/run` to retrieve the flag :

`pwn.college{4ftRmPAo1kI7jEq154njpu3Uqgq.dlDN1QDLzQjN0czW}`

### <u><b><i> Explicit Relative Paths, from /</u></b></i>
In this challenge, we learn how to use `.` to navigate directories using relative paths.

To solve this challenge,

I accessed the root directory `/` using  `cd /` and then  invoked the command `./challenge/run` to retrieve the flag :

`pwn.college{8NTWVLsHyAH7W4tl4jF-g80tzUG.dBTN1QDLzQjN0czW}`

### <u><b><i>Implicit Relative Path</u></b></i>

We learn more about using `.` i.e relative paths in this challenge.

We also learn about a very crucial safety measure where linux doesn't run with a naked path. 

In the below example, we get an error `bash: run: command not found` if we use the command ` cd /challenge` and then `run`.

Therefore to solve this challenge, we have to use `./run` after `cd` into the `challenge` directory.

Doing the aforementioned commands gave me the flag :

`pwn.college{wFwkIN86zeaUUqkZl3j4DftkbbF.dFTN1QDLzQjN0czW}`

### <u><b><i>Home Sweet Home</u></b></i>

In this challenge, We learn that every user has a `home`
directory under `/home`

The `home` directory is typically where users store most of their personal files.

The `~` in this prompt is the current working directory, with `~` being shorthand for `/home/hacker`. 

Note :  The expansion of `~` is an absolute path, and only the leading `~` is expanded. This means, for example, that `~/~` will be expanded to `/home/hacker/~ `rather than `/home/hacker/home/hacker`.



To solve this challenge, I ran the command `/challenge/run ~` which give me the output 

`Writing the file to /home/hacker!`

`/challenge/run: line 29: /home/hacker: Is a directory
... and reading it back to you:
cat: /home/hacker: Is a directory`

But since I did not get the flag I tried copying the run file to a random file using the command `/challenge/run ~/tmp` which finally 
gave me the 

flag :

`pwn.college{A1E4AOpazpbMf5nm8JVMS2x72ZY.dNzM4QDLzQjN0czW}`

# End

