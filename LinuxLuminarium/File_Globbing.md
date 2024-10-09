# File Globbing 

This module tackles file globbing.


- [File Globbing](#file-globbing)
  - [Matching with \*](#matching-with-)
  - [Matching with ?](#matching-with--1)
  - [Matching with \[\]](#matching-with--2)
  - [Matching paths with \[\]](#matching-paths-with-[])
  - [Missing globs](#missing-globs)
  - [Exclusionary globbing](#exclusionary-globbing)
  


## Matching with * 

The first glob we'll learn is *. When it encounters a * character in any argument, the shell will treat it as "wildcard" and try to replace that argument with any files that match the pattern. It's easier to show you than explain:


 
In this challenge, we are supposed to change our cwd to `/challenge` and execute the `run` file to get our flag. But we can only pass in 4 characters to the cd command.

I run the command `cd /ch*` to change my cwd to `/challenge` and then I execute `./run` to get the flag.

The flag : `pwn.college{YwYMBsNrGCNK24mSi1MHS3A0-kh.dFjM4QDLzQjN0czW}`

```
You ran me with the working directory of /challenge! Here is your flag:
pwn.college{YwYMBsNrGCNK24mSi1MHS3A0-kh.dFjM4QDLzQjN0czW}
```

## Matching with ? 

When the shell encounters a `?` character in any argument, the shell will treat it as single-character wildcard. This works like *, but only matches one character. 

To solve this challenge, we are suppposed to change our cwd to `/challenge` and execute the `run` file to get our flag. But we need to use the `?` character instead of c and l in the argument to cd.

I run the command `cd /?ha??enge` to change my cwd to `/challenge` and execute the `./run` file to get the 

Flag : `pwn.college{E88ZFNrKShWnj1_NHASGlgdBjw-.dJjM4QDLzQjN0czW}`



```
hacker@globbing~matching-with-:~$ cd /?ha??enge
hacker@globbing~matching-with-:/challenge$ ./run
You ran me with the working directory of /challenge! Here is your flag:
pwn.college{E88ZFNrKShWnj1_NHASGlgdBjw-.dJjM4QDLzQjN0czW}
```


## Matching with []

 The square brackes are, essentially, a limited form of ?, in that instead of matching any character, [] is a wildcard for some subset of potential characters, specified within the brackets. For example, [pwn] will match the character p, w, or n.


To solve this challenge, we are supposed to change our cwd to `/challenge/files` and execute the `run` file with a single argument that bracket-globs into file_b, file_a, file_s, and file_h.

I ran `cd /challenge/files` to change my cwd to `/challenge/files`. 

We can use `[]` globbing to include `file_a, file_b, file_s, file_h` so I run `/challenge/run file_[bash]` to get the

Flag : `pwn.college{QjzAaYquRNM6XwswRy1eqEq_ujf.dNjM4QDLzQjN0czW}`

```
hacker@globbing~matching-with-:~$ cd /challenge/files
hacker@globbing~matching-with-:/challenge/files$ /challenge/files
ssh-entrypoint: /challenge/files: Is a directory
hacker@globbing~matching-with-:/challenge/files$ file_a, file_b, file_s, file_h
ssh-entrypoint: file_a,: command not found
hacker@globbing~matching-with-:/challenge/files$ /challenge/run file_[bash]
You got it! Here is your flag!
pwn.college{QjzAaYquRNM6XwswRy1eqEq_ujf.dNjM4QDLzQjN0czW}
```
## Matching paths with []

Globbing happens on a path basis, so you can expand entire paths with your globbed arguments.

As with the previous challenge, we are supposed to execute `/challenge/run` with a single argument that bracket-globs into the absolute paths to the file_b, file_a, file_s, and file_h files but from our home directory.

I run `/challenge/run/challenge/files/file_[bash]` to get the flag.

```
hacker@globbing~matching-paths-with-:~$ /challenge/run /challenge/files/file_[bash]
You got it! Here is your flag!
pwn.college{U53rnanKNJkEkDWdp00Jlfjq3AK.dRjM4QDLzQjN0czW}
hacker@globbing~matching-paths-with-:~$
```
The flag : `pwn.college{U53rnanKNJkEkDWdp00Jlfjq3AK.dRjM4QDLzQjN0czW}`

## Missing globs

 TO solve this challenge, we are supposed to change our cwd to `/challenge/files` and execute the `/challenge/run` file with a single argument that bracket-globs into "challenging", "educational", and "pwning" files.

I run `cd /challenge/files` to change my cwd to `/challenge/files`. 

The argument had to less than or equal to 6 characters So I ran `/challenge/run [cep]*` to the flag.

```
hacker@globbing~mixing-globs:~$ cd /challenge/files
hacker@globbing~mixing-globs:/challenge/files$ /challenge/run [cep]*
You got it! Here is your flag!
pwn.college{oY0Ml0HbaGTcx3k-_EBHLUj8xVA.dVjM4QDLzQjN0czW}
```

The flag : `pwn.college{oY0Ml0HbaGTcx3k-_EBHLUj8xVA.dVjM4QDLzQjN0czW}`


## Exclusionary globbing

Sometimes, you want to filter out files in a glob! Luckily, [] helps you do just this. If the first character in the brackets is a ! or (in newer versions of bash) a ^, the glob inverts, and that bracket instance matches characters that aren't listed.

To solve his challenge,  we are asked  to change our cwd to `/challenge/files` and execute the `/challenge/run` file with a single argument that bracket-globs into every file that does not start with p,w and n.

I run `cd /challenge/files` to change my cwd to `/challenge/files`. 

We can use `!` to invert the glob so that it ignores the files that start with p,w and n. Therefore I run `/challenge/run [!pwn]*` to get the flag.

```
hacker@globbing~exclusionary-globbing:~$ cd /challenge/files
hacker@globbing~exclusionary-globbing:/challenge/files$ /challenge/run [!pwn]*
You got it! Here is your flag!
pwn.college{sKcU5HNx1aQC4ZNjw5G78hWJVy9.dZjM4QDLzQjN0czW}
```

The flag : `pwn.college{sKcU5HNx1aQC4ZNjw5G78hWJVy9.dZjM4QDLzQjN0czW}`

# END
