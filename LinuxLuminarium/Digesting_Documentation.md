# <b><i>DIGESTING DOCUMENTATION 
 
In this module, we learn how to read, understand, and retrieve usable information from documentation about various Linux commands.


## Challenges :</b></i>

# Index For Digesting Documentation

1. [Learning From Documentation](#learning-from-documentation)
2. [Learning complex usage](#learning-complex-usage)
3. [Reading Manuals](#reading-manuals)
4. [Searching Manuals](#searching-manuals)
5. [Searching For Manuals](#searching-for-manuals)
6. [Helpful Programs](#helpful-programs)
7. [Help For Builtins](#help-for-builtins)
   


### <b> Learning From Documentation

To solve this challenge, all I had to do was run the command `/challenge/challenge --giveflag` as specified in the documentation.

```Connected!
hacker@man~learning-from-documentation:~$ /challenge/challenge --giveflag
Correct argument! Here is your flag:
pwn.college{M0rSZ-uwR_9lgF5lbtyxCw0jbGI.dRjM5QDLzQjN0czW}
hacker@man~learning-from-documentation:~$

```

The flag : `pwn.college{M0rSZ-uwR_9lgF5lbtyxCw0jbGI.dRjM5QDLzQjN0czW}`

---

### Learning complex usage

In this challenge, we give 2 arguments
which are `--printfile`  and `/flag` to `/challenge/challenge` to get the flag.
```hacker@man~learning-complex-usage:~$ /challenge/challenge --printfile /flag
Correct argument! Here is the /flag file:
pwn.college{Emc7bZyKZrQJFtIbJPe39lM7Dhj.dVjM5QDLzQjN0czW}
hacker@man~learning-complex-usage:~$

```

The Flag :
`pwn.college{Emc7bZyKZrQJFtIbJPe39lM7Dhj.dVjM5QDLzQjN0czW}`

----

### Reading Manuals :

1. This level introduces the `man` command. `man` is short for manual, and will display (if available) the manual of the command you pass as an argument.

2. You can scroll around the manpage with your arrow keys and PgUp/PgDn. When you're done reading the manpage, you can hit q to quit.

In this challenge, We are asked to use the `man` command to look for the flag.

So I used the `man challenge` command to get the manual :

```hacker@man~reading-manuals:~$ man challenge

CHALLENGE(1)                                      Challenge Commands                                     CHALLENGE(1)

NAME
       /challenge/challenge - print the flag!

SYNOPSIS
       challenge OPTION

DESCRIPTION
       Output the flag when called with the right arguments.

       --fortune
              read a fortune

       --version
              output version information and exit

       --gusbbo NUM
              print the flag if NUM is 889

AUTHOR
       Written by Zardus.

REPORTING BUGS
       The repository for this dojo: <https://github.com/pwncollege/linux-luminarium/>

SEE ALSO
       man(1) bash-builtins(7)

pwn.college                                            May 2024                                          CHALLENGE(1) 

```
Thus, According the manual I used `/challenge/challenge --gusbbo 889` to get the key.

```
hacker@man~reading-manuals:~$ /challenge/challenge --gusbbo 889
Correct usage! Your flag: pwn.college{gusJHCb88_bHS9P6od5fwW67hfn.dRTM4QDLzQjN0czW}

```
The flag : `pwn.college{gusJHCb88_bHS9P6od5fwW67hfn.dRTM4QDLzQjN0czW}`


----

### Searching Manuals 

You can scroll man pages with the arrow keys (and `PgUp/PgDn`) and search with `/`. After searching, you can hit `n` to go to the next result and `N` to go to the previous result. Instead of `/`, you can use `?` to search backwards!

In this challenge, after sshing, I used `man challenge` to read the manual and then used above mentioned methods to navigate through the manual to obtain the flag.

After using `/flag` to search for the flag keywords i found 
```
 --nijsi
              This argument will give you the flag!
              

```

Thus I used `/challenge/challenge --nijsi` to rertieve the flag :

```
hacker@man~searching-manuals:~$ /challenge/challenge --nijsi
Initializing...
Correct usage! Your flag: pwn.college{U0yFnkMNNCLwOGIp_qp-2baSFiQ.dVTM4QDLzQjN0czW}

```

The flag : ` pwn.college{U0yFnkMNNCLwOGIp_qp-2baSFiQ.dVTM4QDLzQjN0czW}`

---

### Searching For Manuals

To solve this challenge, 
I ran the `man man` command to open up the manual for the man page database. Which yielded :

```  man [man options] [[section] page ...] ...
       man -k [apropos options] regexp ...
       man -K [man options] [section] term ...
       man -f [whatis options] page ...
       man -l [man options] file ...
       man -w|-W [man options] page ...

```
On googling what these meant, I learn that apropos is used to search for commands that we may have forgotten but remmember some keyword of it.

Source : https://www.geeksforgeeks.org/apropos-command-in-linux-with-examples/


 I tried `man -k challenge` which got me to this :
 ```
 hacker@man~searching-for-manuals:~$ man -k challenge
szcpsbozpp (1)       - print the flag!
```

After which I did `man szcpsbozpp` to understand its functionality. It yielded :

```
SYNOPSIS
       challenge OPTION

DESCRIPTION
       Output the flag when called with the right arguments.

       --fortune
              read a fortune

       --version
              output version information and exit

       --szcpsb NUM
              print the flag if NUM is 025


```

Thus After typing `/challenge//challenge --szcpsb 025`
, I got the flag.

```
hacker@man~searching-for-manuals:~$ /challenge/challenge --szcpsb 025
Correct usage! Your flag: pwn.college{szcpsbo02FNKL56zO1CppJB3KbB.dZTM4QDLzQjN0czW}
```
The flag : `pwn.college{szcpsbo02FNKL56zO1CppJB3KbB.dZTM4QDLzQjN0czW}`.

---

### Helpful Programs

Some programs don't have a man page, but might tell you how to run them if invoked with a special argument. Usually, this argument is --help, but it can often be -h or, in rare cases, -?, help, or other esoteric values like /? (though that latter is more frequently encountered on Windows).

To solve this challenge :
I tried the command `/challenge/challenge --help` and I got this output :

```
hacker@man~helpful-programs:~$ /challenge/challenge --help
usage: a challenge to make you ask for help [-h] [--fortune] [-v] [-g GIVE_THE_FLAG] [-p]

optional arguments:
  -h, --help            show this help message and exit
  --fortune             read your fortune
  -v, --version         get the version number
  -g GIVE_THE_FLAG, --give-the-flag GIVE_THE_FLAG
                        get the flag, if given the correct value
  -p, --print-value     print the value that will cause the -g option to give you the flag
hacker@man~helpful-programs:~$

```

After reading it's "documentation/help page",
I used the command `/challenge/challenge -p`to get `22` as the vlaue and then used the command `/challenge/challenge --give-the-value 22` to get the flag.

```
hacker@man~helpful-programs:~$ /challenge/challenge -p
The secret value is: 22

hacker@man~helpful-programs:~$ /challenge/challenge --give-the-flag 22
Correct usage! Your flag: pwn.college{QAbq0HyqaAvz2k2crW3xjHyyqXu.ddjM4QDLzQjN0czW}
hacker@man~helpful-programs:~$

```

The Flag : `pwn.college{QAbq0HyqaAvz2k2crW3xjHyyqXu.ddjM4QDLzQjN0czW}`
 
 ----

 ### Help For Builtins :

 Some commands, rather than being programs with man pages and help options, are built into the shell itself. These are called builtins. Builtins are invoked just like commands, but the shell handles them internally instead of launching other programs. 

 To Solve this challenge,
 Since `challenge` is a builtin not a command in this challenge, I used the `help <builtin> `to get some info on it,

` help challenge`


This gave me information about the function `--secret VALUE` 
which would give me the key if the `VALUE` was correct
and since the value was provided as `"gM1UmVIh"`. All I had to do was `challenge --secret gM1UmVIh` to get the flag.

```
hacker@man~help-for-builtins:~$ help challenge
challenge: challenge [--fortune] [--version] [--secret SECRET]
    This builtin command will read you the flag, given the right arguments!

    Options:
      --fortune         display a fortune
      --version         display the version
      --secret VALUE    prints the flag, if VALUE is correct

    You must be sure to provide the right value to --secret. That value
    is "gM1UmVIh".
hacker@man~help-for-builtins:~$ challenge --secret gM1UmVIh
Correct! Here is your flag!
pwn.college{gM1UmVIhPiVMqHzg2UzKM-I-lfQ.dRTM5QDLzQjN0czW}

hacker@man~help-for-builtins:~$





```

The flag : `pwn.college{gM1UmVIhPiVMqHzg2UzKM-I-lfQ.dRTM5QDLzQjN0czW}`

# END



