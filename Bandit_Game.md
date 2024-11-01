# Bandit Game

First we `ssh` into level 0 using `ssh bandit0@bandit.labs.overthewire.org -p 2220`

## Level 0-1
 
 * Used `cat readme` to get the password for level 1 :
  `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`.

  Then we ssh into the next lvl by changing bandit0 to bandit1 and the new password.

## Level 1-2

* Used `cat ./-` to read the `-` symbol to get the password : `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`.
  
## Level 2-3

`cat "spaces in the filename"` can be used to access the files with spaces in them as u cant directly acces them as cat assumes them as arguments.

Password : `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

## Level 3-4

* Used `cd inhere` to navgate to the directory then used `ls -A` to ingore `.` and `..` to find `...Hiding-From-you` file which I ran to get the next password : `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

## Level 4-5 

* `cd` to `inhere` then used `ls -A -h` to find a bunch of files like `-file00/-file01` etc and after using `cat ./-file00` upto `cat ./-file 07` I got the password.

The password : `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw` 

## Level 5-6

* `cd`ed into `inhere` and used `find -readable -size 1033c` to get the correct file and then `cat`ed that file to get the password : `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

## Level 6-7

* Since I could not find any file, I searched the entire server using `find / -type f -user bandit7 -group bandit6 -size 33c`
but it showed a lot of files whose permission I didnt have so Instead of manually searching I did `find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null` to remove them and got a singe file which I cat to get the password.

```
 find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
bandit6@bandit:~$
```
Password : `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

## Level 7-8

Checking the file size of data.txt, we can see it is huge:

```
bandit7@bandit:~$ du -b data.txt 
4184396 data.txt
```
Since I've already used piping and grepping extensively in Linuxluminarium and the ctfs I used `cat data.txt | grep millionth` which gave me the password.

```
bandit7@bandit:~$ cat data.txt | grep millionth
millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
bandit7@bandit:~$
```

Password : `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

## Level 8-9 

`uniq` is a command that filters input and writes to the output. Specifically, it filters based on identical lines. It has a flag -u, which filters for unique lines (lines that appear only ones). Another interesting functionality is, for example, that it can also count (-c) or only return duplicate lines (-d).

The command is often used with sort. For uniq to filter for unique lines, the lines need to be sorted. sort sorts the lines of a text file. Furthermore, it has flags for sorting in reverse (-r) and sorting numerically (-n).

I used website's useful commands for this challenge to learn about this.

To find the line that occurs only once in the file, we first sort the lines and then filter for the unique one.

So basically I used `sort data.txt | uniq -u ` to get the password.

```
bandit8@bandit:~$ sort data.txt | uniq -u
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```
>I tried Grep but it just gave huge wall of text.

Password : `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

## Level 9-10

We can use `strings` to lookup human readable text and grep it for the `===` precedence pattern.
I know about strings because I used it in a previous CTF.
So I use `strings data.txt | grep ====` to get the password.

```
bandit9@bandit:~$ strings data.txt | grep ===
}========== the
3JprD========== passwordi
~fDV3========== is
D9========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
bandit9@bandit:~$
```

The password : `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`.

## Level 10-11







