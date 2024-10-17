# Untangling Users

This module is about users.


- [Untangling Users](#untangling-users)
  - [Becoming root with su](#becoming-root-with-su)
  - [Other users with su](#other-users-with-su)
  - [Cracking passwords](#cracking-passwords)
  - [Using su](#using-su)



## Becoming root with su 

In this challenge, we have to start a root shell in order to get our flag.

I run `su` and provide the password `hack-the-planet` to start the root shell.

Then I run `cat /flag` in the root shell to get the flag : `pwn.college{E8ZMh33p81Gff1jYq-FaPuDcwe0.dVTN0UDLzQjN0czW}`


## Other users with su

In this challenge, we have to switch the user to `zardus` and run `/challenge/run` to get our flag.

I run **`su zardus`** and provie the password - `dont-hack-me` to switch to the user to `zardus` 

Then I run **`/challenge/run`** to get the flag : `pwn.college{UJCU4djfw8-TF6GF0rz5bHGVUob.dZTN0UDLzQjN0czW}`

## Cracking passwords

In this challenge, we have to crack the password for the `zardus` user in the `/challenge/shadow-leak` file and login to the `zardus` user.


 * We can use the popular [John The Ripper](https://www.openwall.com/john/) to crack the leaked shadow file and get the password.

I run **`john /challenge/shadow-leak`** and get the password: 

```
Connected!
hacker@users~cracking-passwords:~$ john /challenge/shadow-leak
Created directory: /home/hacker/.john
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
aardvark         (zardus)
1g 0:00:00:20 100% 2/3 0.04899g/s 285.3p/s 285.3c/s 285.3C/s Johnson..buzz
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
Then I logged into `zardus` using `su` and used `/challenge/run` to get the flag  : `pwn.college{YoL0lgicy_50hFy2GiOJ3erwH6h.ddTN0UDLzQjN0czW}`


## Using su

In this challenge, we are supposed to use `sudo` to read the flag. 

I run `sudo cat /flag` to get the flag : `pwn.college{Eg7jt_Xy3tQeCFcxUvMaunqOXD6.dhTN0UDLzQjN0czW}`

# END