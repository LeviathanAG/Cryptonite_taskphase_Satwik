# Perceiving Permissions

This module is about perceiving permissions in Linux.


- [Perceiving Permissions](#perceiving-permissions)
  - [Changing File Ownership](#changing-file-ownership)
  - [Groups and files](#groups-and-files)
  - [Fun With Group Names](#fun-with-group-names)
  - [Changing Permissions](#changing-permissions)
  - [Executable Files](#executable-files)
  - [Permission Tweaking Practice](#permission-tweaking-practice)
  - [Permisson Setting Practice](#permisson-setting-practice)
  - [The SUID Bit](#the-suid-bit)
  
 
## Changing File Ownership

In this challenge, we have to change the owner of the `/flag` file as the `hacker` user in order to access the flag and hence get it. 


* The `chown` command can typically only be used by the `root` user.

 * I run `chown hacker /flag` to change the owner of `/flag` as `hacker`. 

 * Then I run `cat /flag` to print out the flag as I can access it now.

The flag : `pwn.college{8TlncH2glZvroGChUbgoECrcszV.dFTM2QDLzQjN0czW}`

```
Connected!
hacker@permissions~changing-file-ownership:~$ chown hacker /flag
hacker@permissions~changing-file-ownership:~$ cat /flag
pwn.college{8TlncH2glZvroGChUbgoECrcszV.dFTM2QDLzQjN0czW}
hacker@permissions~changing-file-ownership:~$

```

## Groups and files

In this challenge, the `/flag` file is owned by `root` user and only members of the `root` group can access it. We need to change the group owner to `hacker` in order to access it.


* The `chgroup` command can be used to change group ownership. It can typically only be used by the `root` user.

I run `chgrp hacker /flag` to change the group ownership. 

Then I run `cat /flag` to print the flag :
`pwn.college{EIoePM9YgSCnDiYOKcewpE-6tdK.dFzNyUDLzQjN0czW}`


## Fun With Group Names

In this challenge, we need to change the group owner of the file `/flag` to the group which our user `hacker` belongs to, in order to get our flag

I use the `id` command to find out which group `hacker` belongs to :
 
 ```
 hacker@permissions~fun-with-groups-names:~$ id
uid=1000(hacker) gid=1000(grp25662) groups=1000(grp25662)
hacker@permissions~fun-with-groups-names:~$
```
The group `hacker` belongs to is `grp25662` so I run `chgrp grp25662 /flag` to change the group ownership.

Finally I run `cat /flag` to get the flag - `pwn.college{MVOePAS9QWfhihd73-PooRtlZfC.dJzNyUDLzQjN0czW}`


## Changing Permissions


In this challenge, we need to modify the permissions of the file `/flag` in order to get our flag.


* `chmod` allows you to tweak permissions with the mode format of `WHO+/-WHAT`, where `WHO` is user/group/other and `WHAT` is read/write/execute.

I run `chmod o+r /flag` to allow all the users to read the file. 

Then I run `cat /flag` to print out the flag :

`pwn.college{YyaKeYmU8yUJM-sbhbrnloB5F-8.dNzNyUDLzQjN0czW}`

## Executable Files

In this challenge, we need to modify the permissions of the file `/flag` in order to get our flag.

* The file is owned by `hacker` but the owner doesn't have execution permissions so we can run `chmod u+x /challenge/run` to give the owner permission to run the file.

Then I run `/challenge/run` which gives me the flag : 
`pwn.college{kXm7Cw0wI_vyq4ht5830eXRPkly.dJTM2QDLzQjN0czW}`

```
Connected!
hacker@permissions~executable-files:~$ chmod u+x /challenge/run
hacker@permissions~executable-files:~$ /challenge/run
Successful execution! Here is your flag:
pwn.college{kXm7Cw0wI_vyq4ht5830eXRPkly.dJTM2QDLzQjN0czW}
hacker@permissions~executable-files:~$


```

## Permission Tweaking Practice

We need to change the permissions of the /challenge/pwn file in specific ways a few times in a row in order to get our flag.

**Round 0:**
```
Current permissions of "/challenge/pwn": rw-r--r--
Needed permissions of "/challenge/pwn": rw-rw-r--
```
I run `chmod g+w /challenge/pwn` to set the required permissions

**Round 1:**
```
Current permissions of "/challenge/pwn": rw-rw-r--
Needed permissions of "/challenge/pwn": ------r--
```
I run `chmod ug-rw /challenge/pwn` to set the required permissions

**Round 2:**
```
Current permissions of "/challenge/pwn": ------r--
Needed permissions of "/challenge/pwn": ------rw-
```
I run `chmod o+w /challenge/pwn` to set the required permissions

**Round 3:**
```
Current permissions of "/challenge/pwn": ------rw-
Needed permissions of "/challenge/pwn": ---------
```
I run `chmod o-rw /challenge/pwn` to set the required permissions

**Round 4:**
```
Current permissions of "/challenge/pwn": ---------
Needed permissions of "/challenge/pwn": rwxrwxrwx
```
I run `chmod ugo+rwx /challenge/pwn` to set the required permissions

**Round 5:**
```
Current permissions of "/challenge/pwn": rwxrwxrwx
Needed permissions of "/challenge/pwn": -w--w-rwx
```
I run `chmod u-rx,g-rx /challenge/pwn` to set the required permissions

**Round 6:**
```
Current permissions of "/challenge/pwn": -w--w-rwx
Needed permissions of "/challenge/pwn": -w-rw-rwx
```
I run `chmod g+r /challenge/pwn` to set the required permissions

**Round 7:**
```
Current permissions of "/challenge/pwn":  -w-rw-rwx
Needed permissions of "/challenge/pwn":  -wxrwxrwx
```
I run `chmod u+x,g+x /challenge/pwn` to set the required permissions

Finally I run `chmod u+r /flag` to make the flag readable and run `cat /flag` to get the flag - `pwn.college{EYcfK6GrQnQTRUZnKAhlEWWt6_l.dBTM2QDLzQjN0czW}`


## Permisson Setting Practice

We need to change the permissions of the /challenge/pwn file in specific ways a few times in a row in order to get our flag.

```
hacker@permissions~permissions-setting-practice:~$ chmod u=rx,o=rw /challenge/pwn
NEEDED, BUT UNMET permissions of "/challenge/pwn": rw-r-x--x
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

CURRENT, INCORRECT permissions of "/challenge/pwn": r-xr--rw-
* the user does have read permissions
- the user doesn't have write permissions
* the user does have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

You set the permissions incorrectly! Restarting the game!
hacker@permissions~permissions-setting-practice:~$ chmod chmod u=rw,g=rx,o=x /challenge/pwn
/usr/bin/chmod: invalid mode: ‘chmod’
Try '/usr/bin/chmod --help' for more information.
NEEDED, BUT UNMET permissions of "/challenge/pwn": rw-r-x--x
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

CURRENT, INCORRECT permissions of "/challenge/pwn": rw-r--r--
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
- the world doesn't have execute permissions

You set the permissions incorrectly! Restarting the game!
hacker@permissions~permissions-setting-practice:~$ chmod u=rw,g=rx,o=x /challenge/pwn
You set the correct permissions!
Round 1 (of 8)!

Current permissions of "/challenge/pwn": rw-r-x--x
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": -wxrwxr-x
- the user doesn't have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=wx,g=rwx,o=rx /challenge/pwn
You set the correct permissions!
Round 2 (of 8)!

Current permissions of "/challenge/pwn": -wxrwxr-x
- the user doesn't have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": -w-----wx
- the user doesn't have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
* the world does have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=w,g=,o=wx /challenge/pwn
You set the correct permissions!
Round 3 (of 8)!

Current permissions of "/challenge/pwn": -w-----wx
- the user doesn't have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": r---w-rw-
* the user does have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=r,g=w,o=rw /challenge/pwn
You set the correct permissions!
Round 4 (of 8)!

Current permissions of "/challenge/pwn": r---w-rw-
* the user does have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": -wxrw-rw-
- the user doesn't have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=wx,g=rw,o=rw /challenge/pwn
You set the correct permissions!
Round 5 (of 8)!

Current permissions of "/challenge/pwn": -wxrw-rw-
- the user doesn't have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": -w-r--rw-
- the user doesn't have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=w,g=r,o=rw /challenge/pwn
You set the correct permissions!
Round 6 (of 8)!

Current permissions of "/challenge/pwn": -w-r--rw-
- the user doesn't have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": rw-rw-rwx
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
* the world does have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=rw,g=rw,o=rwx /challenge/pwn
You set the correct permissions!
Round 7 (of 8)!

Current permissions of "/challenge/pwn": rw-rw-rwx
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": ---r--rwx
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
* the world does have write permissions
* the world does have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=,g=r,o=rwx /challenge/pwn
You set the correct permissions!
You've solved all 8 rounds! I have changed the ownership
of the /flag file so that you can 'chmod' it. You won't be able to read
it until you make it readable with chmod!

Current permissions of "/flag": ---------
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u+r /flag
hacker@permissions~permissions-setting-practice:~$ cat /flag
pwn.college{8smNuVWl_svyDat161Q-pz6yHwb.dNTM5QDLzQjN0czW}
hacker@permissions~permissions-setting-practice:~$

```

The Flag : `pwn.college{8smNuVWl_svyDat161Q-pz6yHwb.dNTM5QDLzQjN0czW}`

## The SUID Bit

In this challenge, we need to add the SUID bit to `/challenge/getroot` in order to spawn a root shell where we can `cat` out the file.

I run `chmod u+s /challenge/getroot` to add the SUID bit. Then I run `/challenge/getroot` to spawn the root shell.

Finally I run `cat /flag` to get the flag : `pwn.college{cqiBcOeZICZy1YsAtko9rw4Ws2G.dNTM2QDLzQjN0czW}`

```
Connected!
hacker@permissions~the-suid-bit:~$ chmod u+s /challenge/getroot
hacker@permissions~the-suid-bit:~$ /challenge/getroot
SUCCESS! You have set the suid bit on this program, and it is running as root!
Here is your shell...
root@permissions~the-suid-bit:~# cat /glag
cat: /glag: No such file or directory
root@permissions~the-suid-bit:~# cat /flag
pwn.college{cqiBcOeZICZy1YsAtko9rw4Ws2G.dNTM2QDLzQjN0czW}
root@permissions~the-suid-bit:~#


```

# END