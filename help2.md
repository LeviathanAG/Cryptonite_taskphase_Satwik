# the cat command
this command conactenates whatever argument is provided and if noting is mentioned it simply  returns whatever is present in the terminal

sameeksha03@DESKTOP-965QKSJ:~$  ssh -i ./key hacker@dojo.pwn.college
Connected!
hacker@commands~cat-not-the-pet-but-the-command:~$ cat ~/flag
pwn.college{cUp1f4erQBWt_snGO5n7EGQ7rrn.dFzN1QDL5MTM1czW}





# more catting practice
for this we couldn't change the directory using cd so what we did was cat then <absolute path>

sameeksha03@DESKTOP-965QKSJ:~$  ssh -i ./key hacker@dojo.pwn.college


Connected!

You cannot use the 'cd' command in this level, and must retrieve the flag by
absolute path. Plus, I hid the flag in a different directory! You can find it
in the file /usr/share/mime/flag. Go cat it out **without** cding into that
directory!
hacker@commands~more-catting-practice:~$
hacker@commands~more-catting-practice:~$ cat /usr/share/mime/flag
pwn.college{0OHXaLJQfK6TXM3zJVv0A7rggtr.dBjM5QDL5MTM1czW}



#grepping for a needle in haystack
if the file we want to read is too large and we just want to search for particularly few lines in the file instead of using cat we can use grep. this will help us to find string with that particular substring in the file whose absolute path is mentioned


Connected!
hacker@commands~grepping-for-a-needle-in-a-haystack:~$ grep pwn.college /challenge/data.txt
pwn.college{Ecttw1egpoYsMJ9CtWyCjpRoQKx.ddTM4QDL5MTM1czW}



#listing files
the ls command is used when we want to know what files or directories are there in the argument of 'ls <>'.here on doing ls /challenge we could see that the usual run command was renamed to something else so we ran the file accordingly to get the flag.

sameeksha03@DESKTOP-965QKSJ:~$  ssh -i ./key hacker@dojo.pwn.college
Connected!
hacker@commands~listing-files:~$ ls /challenge
2167-renamed-run-28610  DESCRIPTION.md
hacker@commands~listing-files:~$ /challenge/2167-renamed-run-28610
Yahaha, you found me! Here is your flag:
pwn.college{cm6j6opw7uACTwoQasoM_30ZWaN.dhjM4QDL5MTM1czW}




#touching files
here we learnt how to create files using 'touch' command. firstly we went into a directory tmp using cd command and then we created two files namely 'pwn' and 'college' in it.

Connected!
hacker@commands~touching-files:~$ cd /tmp
hacker@commands~touching-files:/tmp$ touch pwn
hacker@commands~touching-files:/tmp$ touch college
hacker@commands~touching-files:/tmp$ /challenge/run
Success! Here is your flag:
pwn.college{0wMcCCWG8hh6VDbuPG_jrOJSrfa.dBzM4QDL5MTM1czW}



#removing files
if we have excess files in a directory we can use this command to remove them. Here a delet_me file was created inside the home directory and we deleted it using rm command.

Connected!
hacker@commands~removing-files:~$ rm delete_me
hacker@commands~removing-files:~$ /challenge/check
Excellent removal. Here is your reward:
pwn.college{MvT8f5pIUXOIYz708hK-FcxmsdQ.dZTOwUDL5MTM1czW}




#hidden files
so while using ls command it doesn't display all the files it hides the ones which begin with a '.' so to view that we need to use the '-a' with the ls command.we can first go into the '/' directory and then use 'ls -a' command or else we can directly use 'ls -a /' command to get the location of flag file.next to view the contents we need to ise the cat command.

sameeksha03@DESKTOP-965QKSJ:~$  ssh -i ./key hacker@dojo.pwn.college
Connected!
hacker@commands~hidden-files:~$ cd /
hacker@commands~hidden-files:/$ ls -a
.   .dockerenv           bin   challenge  etc   lib    lib64   media  nix  proc  run   srv  tmp  var
..  .flag-3209247525160  boot  dev        home  lib32  libx32  mnt    opt  root  sbin  sys  usr
hacker@commands~hidden-files:/$ cat /.flag-3209247525160
pwn.college{MxIB9KyoWeoGBnofbwWyT0dVyIo.dBTN4QDL5MTM1czW}


#
a lot of patience is required first of all.the clues keep coming up and we need to continuously enter into directory , check contenets and read it to get the next clue until we get the flag.



sameeksha03@DESKTOP-965QKSJ:~$  ssh -i ./key hacker@dojo.pwn.college
Connected!
hacker@commands~an-epic-filesystem-quest:~$ cd /
hacker@commands~an-epic-filesystem-quest:/$ ls
INFO  boot       dev  flag  lib    lib64   media  nix  proc  run   srv  tmp  var
bin   challenge  etc  home  lib32  libx32  mnt    opt  root  sbin  sys  usr
hacker@commands~an-epic-filesystem-quest:/$ cat / INFO
cat: /: Is a directory
Yahaha, you found me!
The next clue is in: /usr/lib/python3/dist-packages/sage/geometry/hyperplane_arrangement

The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
hacker@commands~an-epic-filesystem-quest:/$ cd /usr/lib/python3/dist-packages/sage/geometry/hyperplane_arrangement
hacker@commands~an-epic-filesystem-quest:/usr/lib/python3/dist-packages/sage/geometry/hyperplane_arrangement$ ls -a
.   .MEMO        __pycache__         arrangement.py     hyperplane.py  plot.py
..  __init__.py  affine_subspace.py  check_freeness.py  library.py
hacker@commands~an-epic-filesystem-quest:/usr/lib/python3/dist-packages/sage/geometry/hyperplane_arrangement$ cat / .MEMO
cat: /: Is a directory
Lucky listing!
The next clue is in: /opt/busybox/busybox-1.33.2/include/config/feature/show

The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
hacker@commands~an-epic-filesystem-quest:/usr/lib/python3/dist-packages/sage/geometry/hyperplane_arrangement$ cd /opt/busybox/busybox-1.33.2/include/config/feature/show
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/feature/show$ ls
GIST  script.h  threads.h
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/feature/show$ cat /GIST
cat: /GIST: No such file or directory
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/feature/show$ cat / GIST
cat: /: Is a directory
Lucky listing!
The next clue is in: /opt/radare2/binr/radiff2

The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/feature/show$ cd /opt/radare2/binr/radiff2
hacker@commands~an-epic-filesystem-quest:/opt/radare2/binr/radiff2$ ls -a
.  ..  .TIP  Makefile  meson.build  radiff2  radiff2.c  radiff2.d  radiff2.o
hacker@commands~an-epic-filesystem-quest:/opt/radare2/binr/radiff2$ cat / .TIP
cat: /: Is a directory
Tubular find!
The next clue is in: /usr/lib/llvm-10/lib/clang/10.0.0/include/cuda_wrappers

The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
hacker@commands~an-epic-filesystem-quest:/opt/radare2/binr/radiff2$ cd /usr/lib/llvm-10/lib/clang/10.0.0/include/cuda_wrappers
hacker@commands~an-epic-filesystem-quest:/usr/lib/llvm-10/lib/clang/10.0.0/include/cuda_wrappers$ ls -a
.  ..  .REVELATION  algorithm  complex  new
hacker@commands~an-epic-filesystem-quest:/usr/lib/llvm-10/lib/clang/10.0.0/include/cuda_wrappers$ cat / .REVELATION
cat: /: Is a directory
Yahaha, you found me!
The next clue is in: /opt/angr-management/_internal/angr/procedures/stubs/__pycache__

Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
hacker@commands~an-epic-filesystem-quest:/usr/lib/llvm-10/lib/clang/10.0.0/include/cuda_wrappers$ ls /opt/angr-managemen
t/_internal/angr/procedures/stubs/__pycache__
CallReturn.cpython-312.pyc             ReturnChar.cpython-312.pyc              b64_decode.cpython-312.pyc
NUGGET-TRAPPED                         ReturnUnconstrained.cpython-312.pyc     caller.cpython-312.pyc
NoReturnUnconstrained.cpython-312.pyc  UnresolvableCallTarget.cpython-312.pyc  crazy_scanf.cpython-312.pyc
Nop.cpython-312.pyc                    UnresolvableJumpTarget.cpython-312.pyc  format_parser.cpython-312.pyc
PathTerminator.cpython-312.pyc         UserHook.cpython-312.pyc                syscall_stub.cpython-312.pyc
Redirect.cpython-312.pyc               __init__.cpython-312.pyc
hacker@commands~an-epic-filesystem-quest:/usr/lib/llvm-10/lib/clang/10.0.0/include/cuda_wrappers$ cat /opt/angr-management/_internal/angr/procedures/stubs/__pycache__/NUGGET-TRAPPED
Tubular find!
The next clue is in: /opt/capstone/packages/freebsd/ports/devel/capstone

The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
hacker@commands~an-epic-filesystem-quest:/usr/lib/llvm-10/lib/clang/10.0.0/include/cuda_wrappers$ cd /opt/capstone/packages/freebsd/ports/devel/capstone
hacker@commands~an-epic-filesystem-quest:/opt/capstone/packages/freebsd/ports/devel/capstone$ ls
EVIDENCE  Makefile  pkg-descr  pkg-plist
hacker@commands~an-epic-filesystem-quest:/opt/capstone/packages/freebsd/ports/devel/capstone$ cat / EVIDENCE
cat: /: Is a directory
Great sleuthing!
The next clue is in: /usr/share/racket/pkgs/racket-doc/json/compiled
hacker@commands~an-epic-filesystem-quest:/opt/capstone/packages/freebsd/ports/devel/capstone$ cd /usr/share/racket/pkgs/racket-doc/json/compiled
hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/racket-doc/json/compiled$ ls
SNIPPET  info_rkt.dep  info_rkt.zo  json_scrbl.dep  json_scrbl.zo
hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/racket-doc/json/compiled$ cat / SNIPPET
cat: /: Is a directory
Great sleuthing!
The next clue is in: /opt/ghidra/Ghidra/Debug/Debugger-agent-lldb
hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/racket-doc/json/compiled$ cd /opt/ghidra/Ghidra/Debug/Debugger-agent-lldb
hacker@commands~an-epic-filesystem-quest:/opt/ghidra/Ghidra/Debug/Debugger-agent-lldb$ ls
CUE  LICENSE.txt  Module.manifest  lib
hacker@commands~an-epic-filesystem-quest:/opt/ghidra/Ghidra/Debug/Debugger-agent-lldb$ cat / CUE
cat: /: Is a directory
CONGRATULATIONS! Your perserverence has paid off, and you have found the flag!
It is: pwn.college{8iz_Sh8bRKg28PNtH41SV_znOZw.dljM4QDL5MTM1czW}







#making directories 
here we use the mkdir command to create a directory pwn next we go into the directory using cd command and make a file named college using touch command.
just to check if the file has been created or not i have used the ls command.

sameeksha03@DESKTOP-965QKSJ:~$  ssh -i ./key hacker@dojo.pwn.college
Connected!
hacker@commands~making-directories:~$ cd /tmp
hacker@commands~making-directories:/tmp$ mkdir pwn
hacker@commands~making-directories:/tmp$ cd pwn
hacker@commands~making-directories:/tmp/pwn$ touch college
hacker@commands~making-directories:/tmp/pwn$ ls
college
hacker@commands~making-directories:/tmp/pwn$ /challenge/run
Success! Here is your flag:
pwn.college{AL970vxMe4GjCZZAgKC3oPo9UpW.dFzM4QDL5MTM1czW}



#finding files
here i used find command with specifying the name of the file that is 'flag'. it gave me a list of paths which led to flag file.i read the contents one by one of which permission wasn't denied until i got the flag.


hacker@commands~finding-files:~$ find / -name flag
find: ‘/tmp/tmp.MiOQGWw5Zc’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
/usr/local/lib/python3.8/dist-packages/pwnlib/flag
/usr/local/share/radare2/5.9.5/flag
/usr/share/racket/pkgs/errortrace-lib/errortrace/lang/compiled/flag
find: ‘/var/cache/apt/archives/partial’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
find: ‘/var/cache/private’: Permission denied
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/mysql-files’: Permission denied
find: ‘/var/lib/private’: Permission denied
find: ‘/var/lib/mysql’: Permission denied
find: ‘/var/lib/mysql-keyring’: Permission denied
find: ‘/var/lib/php/sessions’: Permission denied
find: ‘/var/log/private’: Permission denied
find: ‘/var/log/apache2’: Permission denied
find: ‘/var/log/mysql’: Permission denied
find: ‘/run/mysqld’: Permission denied
find: ‘/run/sudo’: Permission denied
find: ‘/root’: Permission denied
/opt/pwndbg/.venv/lib/python3.8/site-packages/pwnlib/flag
/opt/radare2/libr/flag
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/1/task/1/fd’: Permission denied
find: ‘/proc/1/task/1/fdinfo’: Permission denied
find: ‘/proc/1/task/1/ns’: Permission denied
find: ‘/proc/1/fd’: Permission denied
find: ‘/proc/1/map_files’: Permission denied
find: ‘/proc/1/fdinfo’: Permission denied
find: ‘/proc/1/ns’: Permission denied
find: ‘/proc/7/task/7/fd’: Permission denied
find: ‘/proc/7/task/7/fdinfo’: Permission denied
find: ‘/proc/7/task/7/ns’: Permission denied
find: ‘/proc/7/fd’: Permission denied
find: ‘/proc/7/map_files’: Permission denied
find: ‘/proc/7/fdinfo’: Permission denied
find: ‘/proc/7/ns’: Permission denied
/nix/store/1yagn5s8sf7kcs2hkccgf8d0wxlrv5sz-radare2-5.9.0/share/radare2/5.9.0/flag
/nix/store/pmvk2bk4p550w182rjfm529kfqddnvh3-python3.11-pwntools-4.12.0/lib/python3.11/site-packages/pwnlib/flag
hacker@commands~finding-files:~$ cat /usr/local/lib/python3.8/dist-packages/pwnlib/flag
cat: /usr/local/lib/python3.8/dist-packages/pwnlib/flag: Is a directory
hacker@commands~finding-files:~$ cat /usr/local/share/radare2/5.9.5/flag
cat: /usr/local/share/radare2/5.9.5/flag: Is a directory
hacker@commands~finding-files:~$ cat /usr/share/racket/pkgs/errortrace-lib/errortrace/lang/compiled/flag




# linking files

sameeksha03@DESKTOP-965QKSJ:~$ ssh -i ./key hacker@dojo.pwn.college
Connected!
hacker@commands~linking-files:~$ ln -s /flag /home/hacker/not-the-flag
ln: failed to create symbolic link '/home/hacker/not-the-flag': File exists
hacker@commands~linking-files:~$ /challenge/catflag
About to read out the /home/hacker/not-the-flag file!
pwn.college{I_DespzLO7n3rUnepNk4spPGxtN.dlTM1UDL5MTM1czW}
pwn.college{Mp89SXWWvJg-zVPuuQrlNtBQEbN.dJzM4QDL5MTM1czW}hacker@commands~finding-files:~$
