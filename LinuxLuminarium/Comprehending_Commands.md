### <i><b>COMPREHENDING COMMANDS

In this module, we learn about useful linux commands annd their usecases.


## cat: Not the pet, but the command:</b></i>

One of the most critical Linux commands is cat. cat is most often used for reading out files.

cat will concatenate (hence the name) multiple files if provided multiple arguments.

If you give no arguments at all, cat will read from the terminal input and output it.

In this challenge,
the flag was in the flag file in the `~` home directory basically.




I ran the `cat flag` command in the `~` home directory to get the flag.



The flag : `pwn.college{kL7G5s8n5WUjuI1hyOwM7BYY7UJ.dFzN1QDLzQjN0czW}`


## Catting absolute paths

In this challenge, the file to be read wasn't in the home folder so according to the challenge I read it by specifying the absolute path in the argument i.e `cat /flag` to get the flag :



The flag : `pwn.college{kcb11gRNs7WW__0X6FVLtkdz56q.dlTM5QDLzQjN0czW}`





## More catting Practice

In this challenge, I had to give absolute paths as arguments to the `cat` command and `cd` was disabled and when I started the challenge


 typed the command `cat /lib/php/flag` to read and retrieve the flag.



The flag:
`pwn.college{M9ZKYPYK1erGcdajAEykqdvYQGs.dBjM5QDLzQjN0czW}`


## grepping For A Needle In A Haystack

When the files we `cat` are too big to read, we can use `grep`.

`Thought Process:`

In this challenge, we had to implement `grep` to get the flag.
The given path was `/challenge/data.txt`.

They also gave us the search_string arguement as pwn.college.

Thus, I used the command `grep pwn.college /challenge/data.txt` to retrieve the flag.




The flag :
`pwn.college{EeZ_crwai4zHh6Oeo991aRyTC9w.ddTM4QDLzQjN0czW}`

## Listing files

In this challenge, we learn the `ls` command to list the files in a directory.

`ls` will list files in all the directories provided to it as arguments, and in the current directory if no arguments are provided.

To solve this challenge, I had to list the files in the /challenge directory using `ls /challenge` which gave me two files :



I ran the command `/challenge/725-renamed-run-31377` which gave me the flag:



The flag : `pwn.college{csrftNXhjjijOLLo0oAcogZeKvc.dhjM4QDLzQjN0czW}`

## touching files

In this challenge, we had to create two files `pwn` and `college` in the tmp directory by `cd`ing into the `tmp` directory.

I used the command `cd /tmp` and then `touch pwn` and `touch college` to create new files in `/tmp` and ran the command `/challenge/run` to get the flag



The flag :

`pwn.college{YLf4OXDMwOedM96oZfWFE_uCBSu.dBzM4QDLzQjN0czW}`

## Removing files

In this challenge, we learn about `rm` which removes/deletes files.

To solve the challenge,
I had to `rm delete_me` to delete the file in the `~` or /home directory and run `/challenge/check` to retrieve the flag.



The flag : `pwn.college{gpP6tp9VlcomO5OJT42o3_cz2E6.dZTOwUDLzQjN0czW}`
## Hidden files

`ls` doesn't list all the files by default. Linux has a convention where files that start with a `.` don't show up by default in `ls` and in a few other contexts.

 To view them with `ls`, you need to invoke `ls` with the `-a` flag
 
 To solve this challenge which was to find the hidden file,

 I ran the command `cd /` to go the `/` directory as specified in the challenge and then ran the command `ls -a` to view the list of files including the hidden ones which gave me some files.


 I tried the command `/.flag-38041226126017` which didn't work then I realised I can read the `.flag-38041226126017` file with `cat`.
 
  Thus I ran the command `.flag-38041226126017` to retrieve the flag :

 

 The flag : `pwn.college{IBXRlfd1f307JlBqGRhsV4xSati.dBTN4QDLzQjN0czW}`

 ## An Epic Filesystem Quest

 Using all the previous commands, I set out to solve this "game".

 I first `cd`ed to the `/` directory.
 
 Then I used the `ls` command which didn't yield me anything worthwhile and then I tried `ls -a` which gave me a `README` file and then I ran `cat README` to read the file which give me a new file locations as a clue.

 

 With the new clues, I navigated to the give directory
 using `cd /opt/linux/linux-5.4/drivers/gpu/drm/nouveau/nvkm/engine/ce`
  
and then ran `ls -a` to get the next clue.



Next, I ran the command `cat .SPOILER` which gave me this output :



I also tried `cat`ing/`cd`ing to other random files but found nothing of importance.

Now, I ran the command `cd /usr/lib/python3/dist-packages/future/moves/dbm/__pycache__` along with `ls -a` to get a new file.



Then, I ran the command `cat DOSSIER` to get the next clue.


I used to `cd /usr/share/racket/pkgs/typed-racket-doc/typed-racket/scribblings/reference/compiled` according to the next clue and used `ls -a` to get a new file.



I `cd`ed to the next one and `ls -a`ed a bunch more times to find a clue which self-destructed if I would `cd` into the directory: 


 So I used `ls -a /usr/share/racket/pkgs/math-lib/math/private/compiled`  to get the file.
 
 
 AFTER I ran the INFO-TRAPPED FILE WITHOUT `cd`ing into it using
 
  `cat /usr/share/racket/pkgs/math-lib/math/private/compiled/INFO_TRAPPED` 

  I got another Path to which I `cd`,`ls -a`
and `cat`ted a file to finally secure the flag :


The flag :

`pwn.college{kj6fZq4LjUXjM25DMPgM-TQWa2_.dljM4QDLzQjN0czW}`

## making Directories

You can make directories using the `mkdir` command.

To sovle this challenge, I used `cd /tmp`
to `cd` into `tmp` and then used `mkdir pwn` to make a directory and then `cd /tmp/pwn` to `cd` into the directory and then used `touch college` to make a file and then ran `/challenge/check` to retrieve the flag:


The flag:

`pwn.college{QE0o9I_kr3UQm5Vn1IRWMyZKtPB.dFzM4QDLzQjN0czW}`

## Finding files

We use the `find` command to find files.

The `find` command takes optional arguments describing the search criteria and the search location. If you don't specify a search criteria, find matches every file. If you don't specify a search location, find uses the current working directory `(.)`.

To solve the challenge, I `cd`ed into `/` and then ran `find -name flag` and got a bunch of directories and files and after just copying pasting these into the terminal I was able to understand whether they were a file or a directory and then used `ls -a` and `cat` suitably to get the flag :



The flag :


`pwn.college{owddE55MKhAdhFGeXWLvtOnHq7v.dJzM4QDLzQjN0czW}`

## Linking files

In this challenge, we learn about linking.

Links come in two flavors: hard and soft (also known as symbolic) links.

To solve this challenge, I tried `/challenge/catfalg` but to no avail, I tried `ln -s /flag /home/hacker/not-the-flag` and then tried the `/challenge/catflag`
which gave me the flag.

The flag :

`pwn.college{cs1gVEd5Ke4fukDzgEUIdSf-zru.dlTM1UDLzQjN0czW}`
______
# End




