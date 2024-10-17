# Shell Variables

- [Shell Variables](#shell-variables)
  - [Printing Variables](#printing-variables)
  - [Setting Variables](#setting-variables)
  - [Multi-word Variables](#multi-word-variables)
  - [Exporting Variables](#exporting-variables)
  - [Printing Exported Variables](#printing-exported-variables)
  - [Storing Command Output](#storing-command-output)
  - [Reading Input](#reading-input)
  - [Reading Files](#reading-files)
  
## Printing Variables 

  I had to print out the variable `FLAG` to get the flag.

  I printed out the variable with echo by prepending the variable name with `$`. Running `echo $FLAG` which gave me
 
  The flag : `pwn.college{MPVQ7zHkp3sKHlBguU0dtUMmeTf.ddTN1QDLzQjN0czW}`

   ```
    hacker@variables~printing-variables:~$ echo $FLAG
           pwn.college{MPVQ7zHkp3sKHlBguU0dtUMmeTf.ddTN1QDLzQjN0czW}
    

   ```

## Setting Variables

   To solve this challenge, we are supposed to write the value `COLLEGE` to the variable `PWN` to get our flag.

   

   We can set the `PWN` variable to `COLLEGE` by running **`PWN=COLLEGE`** which gives us the flag.
   
    The flag - `pwn.college{AG38-ZFpS9ltAgUg2WAUG7UcueK.dlTN1QDLzQjN0czW}` 


## Multi-word Variables

   In this challenge, we are supposed to write the value `COLLEGE YEAH` to the variable `PWN` to get our flag.


   When the shell sees a space, it ends the variable assignment and interprets the next word as a command.

   We can overcome this by quoting the text.

   We can run `PWN="COLLEGE YEAH"` which gives us
   
  The flag - `pwn.college{Q7966D1kT0jTkf2pTYZ0HkNOJC1.dBjN1QDLzQjN0czW}`

## Exporting Variables

To solve this challenge, we must invoke `/challenge/run` with the PWN variable exported and set to the value COLLEGE, and the COLLEGE variable set to the value PWN but not exported.

We can run `export PWN=COLLEGE` to export the `PWN` variable amd we can run `COLLEGE=PWN` to set the `COLLEGE` variable.

But `/challenge/run` has to be run in a shell process where `COLLEGE` variable is not inherited so we can create a child process using `sh` where only the variable `PWN` will be available.

Running `/challenge/run` in the newly created child process gives us the flag.

```
Connected!
hacker@variables~exporting-variables:~$ export PWN=COLLEGE
You've set the PWN variable to the proper value!
hacker@variables~exporting-variables:~$ COLLEGE=PWN
You've set the PWN variable to the proper value!
You've set the COLLEGE variable to the proper value!
hacker@variables~exporting-variables:~$ /challenge/run
CORRECT!
You have exported PWN=COLLEGE and set, but not exported, COLLEGE=PWN. Great
job! Here is your flag:
pwn.college{c2oXwj398mIvd9-JTDXxNrybb7Y.dJjN1QDLzQjN0czW}
You've set the PWN variable to the proper value!
You've set the COLLEGE variable to the proper value!
hacker@variables~exporting-variables:~$
```

The flag : `pwn.college{c2oXwj398mIvd9-JTDXxNrybb7Y.dJjN1QDLzQjN0czW}`



## Printing Exported Variables

In this challenge, we must print out all the exported variables and look for the `FLAG` variable.

We can use the piping concepts we learnt in the previous module and run `env | grep FLAG` which gives us the flag.

```
hacker@variables~printing-exported-variables:~$ env | grep FLAG
FLAG=pwn.college{w4UU9LraEfBvId1P-awarbBJwVZ.dhTN1QDLzQjN0czW}
hacker@variables~printing-exported-variables:~$
```

The flag : `pwn.college{w4UU9LraEfBvId1P-awarbBJwVZ.dhTN1QDLzQjN0czW}`

## Storing Command Output 

In this challenge, we are supposed to store the output of `/challenge/run` in a variable called `PWN` and we must print it out in order to get our flag.

We can run `PWN=$(/challenge/run)` to store the output of `/challenge/run` in `PWN`. We can then use `echo $PWN` to print out our flag : 

```
Connected!
hacker@variables~storing-command-output:~$ PWN=$(/challenge/run)
Congratulations! You have read the flag into the PWN variable. Now print it out
and submit it!
hacker@variables~storing-command-output:~$ echo $PWN
pwn.college{UZ2YcfsSE6mTCTPkAp2YUeuWebs.dVzN0UDLzQjN0czW}
hacker@variables~storing-command-output:~$
```

The flag : `pwn.college{UZ2YcfsSE6mTCTPkAp2YUeuWebs.dVzN0UDLzQjN0czW}`

## Reading Input

In this challenge, we are supposed to use the `read` command to write the value `COLLEGE` to the variable `PWN`.

We can run `read -p "Enter:" PWN` and enter `COLLEGE` which will give us the flag.

```
hacker@variables~reading-input:~$ read -p "Enter:" PWN
Enter:COLLEGE
You've set the PWN variable properly! As promised, here is the flag:
pwn.college{UwmojFFmkwWhCGrEReivr7ofB1e.dhzN1QDLzQjN0czW}
hacker@variables~reading-input:~$
```
The flag : `pwn.college{UwmojFFmkwWhCGrEReivr7ofB1e.dhzN1QDLzQjN0czW}`


## Reading Files

In this challenge, we supposed to read the output of `/challenge/read_me` into `PWN` to get our flag.

We can use the `<` operator we learnt from the previous to pipe the ouput of `/challenge/read_me` into the input stream of `read`. 

Running `read PWN < /challenge/read_me` gave me the flag.

```
Connected!
hacker@variables~reading-files:~$ read PWN < /challenge/read_me
You've set the PWN variable properly! As promised, here is the flag:
pwn.college{k180GxkFl_lxSFomqcISBKWEJPg.dBjM4QDLzQjN0czW}
```

The flag : `pwn.college{k180GxkFl_lxSFomqcISBKWEJPg.dBjM4QDLzQjN0czW}`


# END



    

   

  



