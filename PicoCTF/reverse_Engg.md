# Reverse Engineering
In this Writeup, we learn how to decompile and understand waht happens under the hood when we run files and how to exploit them to get our flags.
## GDB baby step 1

![ida main file](/PicoCTF/imagesforrev/image.png)

 I googled what _fastcall is and understood that it is:

 The __fastcall calling convention specifies that arguments to functions be passed in registers, when possible. The classes in System. Runtime. CompilerServices are for compiler writers' use only.

 The first three parameters are passed (from left to right) in EAX, EDX, and ECX, if they fit in the register

var10 and var4 are basically storing pointers to some address with var10 is pointing to a memory address of 16 bytes.

But this was a very weird tangent but since OASIS ctf and WTFctf taught me to carefully examine challenge titles, I recalled that we could use `GDB` to try to see the state of eax during main.

So first I used  `file debugger0_a` where i got this :

```
satwik@Satwik:~$ file debugger0_a
debugger0_a: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=15a10290db2cd2ec0c123cf80b88ed7d7f5cf9ff, for GNU/Linux 3.2.0, not stripped
```
after googling what all this meant, I understood that this is an executable but thats all redundant what really helped me were : 

```
for GNU/Linux 3.2.0:

This indicates the executable can be run on linux.


not stripped:

This basically means the executable can be dubgged.



```

now i ran the command `strings debugger0_a` but i got nothing useful tbh.

So I dived straight into gdb after seeing this yt video : https://www.youtube.com/watch?v=1iptoUKXrcI

first i ran `chmod u+x debugger0_a` to make it an executable

then `gdb debugger0_a` which gave me :

```
satwik@Satwik:~$ chmod u+x debugger0_a
satwik@Satwik:~$ ./debugger0_a
satwik@Satwik:~$ gdb debugger0_a
GNU gdb (Ubuntu 12.1-0ubuntu1~22.04.2) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from debugger0_a...
(No debugging symbols found in debugger0_a)
```
then I ran `disassemble main` according to the question description and hint 2 and ida but I didnt get this idea until i saw the hint.

The output was basically this :
```
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   rbp
   0x000000000000112e <+5>:     mov    rbp,rsp
   0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001138 <+15>:    mov    eax,0x86342
   0x000000000000113d <+20>:    pop    rbp
   0x000000000000113e <+21>:    ret
   ```
   since the `0x86342` is being stored in the eax register using `mov` that was probably the string.

   I used an online hex to decimal convertor to get : `549698`
 Then I submitted the flag using the format : `picoCTF{549698}` to solve the challenge.

 ![alt text](/PicoCTF/imagesforrev/compgdbbaby1.png)