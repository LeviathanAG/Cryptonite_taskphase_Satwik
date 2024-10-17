# Processes and Jobs

- [Processes and Jobs](#processes-and-jobs)
  - [Listing Processes](#listing-processes)
  - [Killing Processes](#killing-processes)
  - [Interupting Processes](#interupting-processes)
  - [Suspending Processes](#suspending-processes)
  - [Resuming Processes](#resuming-processes)
  - [Backgrounding Processes](#backgrounding-processes)
  - [Foregrounding Processes](#foregrounding-processes)
  - [Starting Backgrounded Processes](#starting-backgrounded-processes)
  - [Process Exit Codes](#process-exit-codes)
  

## Listing Processes

In this challenge, `/challenge/run` has been renamed to a random filename and we must use the process snapshot to find it and hence get our flag.

I run `ps aux` which displays:
```
Connected!
hacker@processes~listing-processes:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.8  0.0   1056   640 ?        Ss   12:49   0:00 /sbin/docker-init -- /nix/var/nix/profiles/default/bi
root           7  0.1  0.0   5052  2560 ?        S    12:49   0:00 /run/dojo/bin/sleep 6h
root          67  0.0  0.0   4132  2560 ?        S    12:49   0:00 /challenge/30704-run-12598
root          71  0.0  0.0   2744  1280 ?        S    12:49   0:00 sleep 6h
hacker        72  0.8  0.0   5240  4160 pts/0    Ss   12:49   0:00 /run/dojo/bin/ssh-entrypoint
hacker        89  0.0  0.0   7868  3520 pts/0    R+   12:49   0:00 ps aux
```
Then I ran `/challenge/30704-run-12598` to get the flag :

`pwn.college{geelkf4gd-s1sWRj8zJERHpv4YV.dhzM4QDLzQjN0czW}`


## Killing Processes

In this challenge, `/challenge/run` will refuse to run while `/challenge/dont_run` is running therefore we must kill the `/challenge/dont_run` process and run `/challenge/run` to get our flag. 

I use `ps aux | grep /challenge/dont_run` which displays:
```
Connected!
hacker@processes~killing-processes:~$ ps aux | grep /challenge/dont_run
hacker        73  0.0  0.0   4976  3200 ?        Ss   12:51   0:00 /challenge/dont_run
hacker        96  0.0  0.0   5656  2880 pts/0    S+   12:51   0:00 /bin/bash /challenge/dont_run
hacker       116  0.0  0.0   4140  2240 pts/1    S+   12:52   0:00 grep --color=auto /challenge/dont_run
hacker@processes~killing-processes:~$

```
The pid of the process is `73` so i kill it using `kill 73`and then i ran `/challenge/run` to get the flag :

```
Great job! Here is your payment:
pwn.college{I4bVoqkNbb2D6mtyc_safDRyWgd.dJDN4QDLzQjN0czW}
hacker@processes~killing-processes:~$
```

The flag : `pwn.college{I4bVoqkNbb2D6mtyc_safDRyWgd.dJDN4QDLzQjN0czW}`

## Interupting Processes

In this challenge, we must "interrupt" the process `/challenge/run` to get our flag.

I run `/challenge/run` to start the process and then hotkey `Ctrl+C` to interrupt the process to get the flag :

```
Connected!
hacker@processes~interrupting-processes:~$ /challenge/run
I could give you the flag... but I won't, until this process exits. Remember,
you can force me to exit with Ctrl-C. Try it now!
^C
Good job! You have used Ctrl-C to interrupt this process! Here is your flag:
pwn.college{k_1ZAUlLylL0nPanowg8wjBSpeL.dNDN4QDLzQjN0czW}
hacker@processes~interrupting-processes:~$
```
The flag : `pwn.college{k_1ZAUlLylL0nPanowg8wjBSpeL.dNDN4QDLzQjN0czW}`

## Suspending Processes

In this challenge, we must suspend the process `/challenge/run` as it requires another copy of it running in the terminal to print out the flag.

I run `/challenge/run` to start the process and then hotkey `Ctrl+Z` to suspend the process. 

Then I run `/challenge/run` again which gives me the flag :
`pwn.college{MzQfWsc84EKANMuEmvrhNz9OqMT.dVDN4QDLzQjN0czW}`

```

Connected!
hacker@processes~suspending-processes:~$ /challenge/run
I'll only give you the flag if there's already another copy of me running in
this terminal... Let's check!

UID          PID    PPID  C STIME TTY          TIME CMD
root          81      64  0 12:58 pts/0    00:00:00 bash /challenge/run
root          83      81  0 12:58 pts/0    00:00:00 ps -f

I don't see a second me!

To pass this level, you need to suspend me and launch me again! You can
background me with Ctrl-Z or, if you're not ready to do that for whatever
reason, just hit Enter and I'll exit!
^Z
[1]+  Stopped                 /challenge/run
hacker@processes~suspending-processes:~$ /challenge/run
I'll only give you the flag if there's already another copy of me running in
this terminal... Let's check!

UID          PID    PPID  C STIME TTY          TIME CMD
root          81      64  0 12:58 pts/0    00:00:00 bash /challenge/run
root          88      64  0 12:59 pts/0    00:00:00 bash /challenge/run
root          90      88  0 12:59 pts/0    00:00:00 ps -f

Yay, I found another version of me! Here is the flag:
pwn.college{MzQfWsc84EKANMuEmvrhNz9OqMT.dVDN4QDLzQjN0czW}
hacker@processes~suspending-processes:~$

```

## Resuming Processes 

In this challenge, we must suspend the process `/challenge/run` and resume it in order to get our flag.

I run `/challenge/run` to start the process and then hotkey `Ctrl+Z` to suspend the process. 

Then I run `fg` to resume the process which gives me the flag :
`pwn.college{0VT9lHDRfv-iRZMtxEicUAubfX8.dZDN4QDLzQjN0czW}`

```
Connected!
hacker@processes~resuming-processes:~$ /challenge/run
Let's practice resuming processes! Suspend me with Ctrl-Z, then resume me with
the 'fg' command! Or just press Enter to quit me!
^Z
[1]+  Stopped                 /challenge/run
hacker@processes~resuming-processes:~$ fg
/challenge/run
I'm back! Here's your flag:
pwn.college{0VT9lHDRfv-iRZMtxEicUAubfX8.dZDN4QDLzQjN0czW}
Don't forget to press Enter to quit me!





```
## Backgrounding Processes

In this challenge, we must run a process of `/challenge/run` in the background and run another process of `/challenge/run` in order to get our flag.

I run `/challenge/run` and hotkey `Ctrl+Z` to suspend the process. Then I run `bg` to make it run in the background.

Finally I run another process of `/challenge/run` which gives me the flag : `pwn.college{MCpZUH5fUpjaesl-ZcWTy2mEZ4C.ddDN4QDLzQjN0czW}`

```
Connected!
hacker@processes~backgrounding-processes:~$ /challenge/run
I'll only give you the flag if there's already another copy of me running *and
not suspended* in this terminal... Let's check!

UID          PID STAT CMD
root          83 S+   bash /challenge/run
root          85 R+   ps -o user=UID,pid,stat,cmd

I don't see a second me!

To pass this level, you need to suspend me, resume the suspended process in the
background, and then launch a new version of me! You can background me with
Ctrl-Z (and resume me in the background with 'bg') or, if you're not ready to
do that for whatever reason, just hit Enter and I'll exit!
^Z
[1]+  Stopped                 /challenge/run
hacker@processes~backgrounding-processes:~$ bg
[1]+ /challenge/run &



hacker@processes~backgrounding-processes:~$ Yay, I'm now running the background! Because of that, this text will probably
overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times
to scroll this text out.
/challenge/run
I'll only give you the flag if there's already another copy of me running *and
not suspended* in this terminal... Let's check!

UID          PID STAT CMD
root          83 S    bash /challenge/run
root          93 S    sleep 6h
root          94 S+   bash /challenge/run
root          96 R+   ps -o user=UID,pid,stat,cmd

Yay, I found another version of me running in the background! Here is the flag:
pwn.college{MCpZUH5fUpjaesl-ZcWTy2mEZ4C.ddDN4QDLzQjN0czW}
hacker@processes~backgrounding-processes:~$
```

## Foregrounding Processes

In this challenge, we must foreground a process of `/challenge/run` running in the background to get our flag.

I run `/challenge/run` and hotkey `Ctrl+Z` to suspend the process. Then I run `bg` to make it run in the background.

Finally I run `fg` to foreground the process. Following the instructions of the program gives me the flag : 
`pwn.college{oDk4xlMfm92aIbLFxYrPcA6_qZg.dhDN4QDLzQjN0czW}`

```
Connected!
hacker@processes~foregrounding-processes:~$ /challenge/run
To pass this level, you need to suspend me, resume the suspended process in the
background, and *then* foreground it without re-suspending it! You can
background me with Ctrl-Z (and resume me in the background with 'bg') or, if
you're not ready to do that for whatever reason, just hit Enter and I'll exit!
^Z
[1]+  Stopped                 /challenge/run
hacker@processes~foregrounding-processes:~$ bg
[1]+ /challenge/run &



Yay, I'm now running the background! Because of that, this text will probably
overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times
to scroll this text out. After that, resume me into the foreground with 'fg';
I'll wait.
hacker@processes~foregrounding-processes:~$ fg
/challenge/run
YES! Great job! I'm now running in the foreground. Hit Enter for your flag!

pwn.college{oDk4xlMfm92aIbLFxYrPcA6_qZg.dhDN4QDLzQjN0czW}
hacker@processes~foregrounding-processes:~$
```

## Starting Backgrounded Processes

In this challenge, we must run `/challenge/run` backgrounded in order to get our flag.


* We can add `&` at the end of a command to run it in the background.

I run `/challenge/run &` and get the flag : 
`pwn.college{Uz4GBOfL3EtHLCqfcquS6u1lSkR.dlDN4QDLzQjN0czW}`

## Process Exit Codes

In this challenge, we must get the exit code of the process `/challenge/get-code` and pass in the exit code as an argument to `/challenge/submit-code` to get our flag.

I run `/challenge/get-code` and then run `echo $?` to get the exit code of the process. The exit code is `53`.

Lastly I run `/challenge/submit-code 53` which gives me the flag :

`pwn.college{gU9LloDt8RGHnzBZ_IciTEHyVK_.dljN4UDLzQjN0czW}`

```
hacker@processes~process-exit-codes:~$ /challenge/get-code
Exiting with an error code!
hacker@processes~process-exit-codes:~$ echo $?
53
hacker@processes~process-exit-codes:~$ /challenge/submit-code 53
CORRECT! Here is your flag:
pwn.college{gU9LloDt8RGHnzBZ_IciTEHyVK_.dljN4UDLzQjN0czW}
hacker@processes~process-exit-codes:~$


```

# END
