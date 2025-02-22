# Reverse Engineering
In this Writeup, we learn how to decompile and understand waht happens under the hood when we run files and how to exploit them to get our flags.

- [Reverse Engineering](#reverse-engineering)
	- [GDB baby step 1](#gdb-baby-step-1)
		
	
	- [ARMssembly 1](#armssembly-1)
	
	
	- [Vault door 3](#vault-door-3)
	- [ASCII FTW](#ascii-ftw)
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

## ARMssembly 1

In this challenge, we're given a file `chall_1.S` which I installed using `wgets` and then ran the basic commands 

```
satwik@Satwik:~/revpico$ ls
chall_1.S
satwik@Satwik:~/revpico$ ./chall_1.S
-bash: ./chall_1.S: Permission denied
satwik@Satwik:~/revpico$ chmod u+x chall_1.S
satwik@Satwik:~/revpico$ ./chall_1.S
./chall_1.S: line 1: .arch: command not found
./chall_1.S: line 2: .file: command not found
./chall_1.S: line 3: .text: command not found
./chall_1.S: line 4: .align: command not found
./chall_1.S: line 5: .global: command not found
./chall_1.S: line 6: .type: command not found
./chall_1.S: line 7: func:: command not found
./chall_1.S: line 8: sub: command not found
./chall_1.S: line 9: str: command not found
./chall_1.S: line 10: mov: command not found
./chall_1.S: line 11: str: command not found
./chall_1.S: line 12: mov: command not found
./chall_1.S: line 13: str: command not found
./chall_1.S: line 14: mov: command not found
./chall_1.S: line 15: str: command not found
./chall_1.S: line 16: ldr: command not found
./chall_1.S: line 17: ldr: command not found
./chall_1.S: line 18: lsl: command not found
./chall_1.S: line 19: str: command not found
./chall_1.S: line 20: ldr: command not found
./chall_1.S: line 21: ldr: command not found
./chall_1.S: line 22: sdiv: command not found
./chall_1.S: line 23: str: command not found
./chall_1.S: line 24: ldr: command not found
./chall_1.S: line 25: ldr: command not found
./chall_1.S: line 26: sub: command not found
./chall_1.S: line 27: str: command not found
./chall_1.S: line 28: ldr: command not found
./chall_1.S: line 29: add: command not found
./chall_1.S: line 30: ret: command not found
./chall_1.S: line 31: .size: command not found
./chall_1.S: line 32: .section: command not found
./chall_1.S: line 33: .align: command not found
./chall_1.S: line 34: .LC0:: command not found
./chall_1.S: line 35: .string: command not found
./chall_1.S: line 36: .align: command not found
./chall_1.S: line 37: .LC1:: command not found
./chall_1.S: line 38: .string: command not found
./chall_1.S: line 39: .text: command not found
./chall_1.S: line 40: .align: command not found
./chall_1.S: line 41: .global: command not found
./chall_1.S: line 42: .type: command not found
./chall_1.S: line 43: main:: command not found
./chall_1.S: line 44: stp: command not found
./chall_1.S: line 45: add: command not found
./chall_1.S: line 46: str: command not found
./chall_1.S: line 47: str: command not found
./chall_1.S: line 48: ldr: command not found
./chall_1.S: line 49: add: command not found
./chall_1.S: line 50: ldr: command not found
./chall_1.S: line 51: bl: command not found
./chall_1.S: line 52: str: command not found
./chall_1.S: line 53: ldr: command not found
./chall_1.S: line 54: bl: command not found
cmp: w0,: No such file or directory
./chall_1.S: line 56: bne: command not found
./chall_1.S: line 57: adrp: command not found
./chall_1.S: line 58: add: command not found
./chall_1.S: line 59: bl: command not found
./chall_1.S: line 60: b: command not found
./chall_1.S: line 61: .L4:: command not found
./chall_1.S: line 62: adrp: command not found
./chall_1.S: line 63: add: command not found
./chall_1.S: line 64: bl: command not found
./chall_1.S: line 65: .L6:: command not found
./chall_1.S: line 66: nop: command not found
./chall_1.S: line 67: ldp: command not found
./chall_1.S: line 68: ret: command not found
./chall_1.S: line 69: .size: command not found
./chall_1.S: line 70: .ident: command not found
./chall_1.S: line 71: .section: command not found
satwik@Satwik:~/revpico$ file chall_1.S
chall_1.S: assembler source, ASCII text
satwik@Satwik:~/revpico$ strings chall_1.S
        .arch armv8-a
        .file   "chall_1.c"
        .text
        .align  2
        .global func
        .type   func, %function
func:
        sub     sp, sp, #32
        str     w0, [sp, 12]
        mov     w0, 79
        str     w0, [sp, 16]
        mov     w0, 7
        str     w0, [sp, 20]
        mov     w0, 3
        str     w0, [sp, 24]
        ldr     w0, [sp, 20]
        ldr     w1, [sp, 16]
        lsl     w0, w1, w0
        str     w0, [sp, 28]
        ldr     w1, [sp, 28]
        ldr     w0, [sp, 24]
        sdiv    w0, w1, w0
        str     w0, [sp, 28]
        ldr     w1, [sp, 28]
        ldr     w0, [sp, 12]
        sub     w0, w1, w0
        str     w0, [sp, 28]
        ldr     w0, [sp, 28]
        add     sp, sp, 32
        ret
        .size   func, .-func
        .section        .rodata
        .align  3
.LC0:
        .string "You win!"
        .align  3
.LC1:
        .string "You Lose :("
        .text
        .align  2
        .global main
        .type   main, %function
main:
        stp     x29, x30, [sp, -48]!
        add     x29, sp, 0
        str     w0, [x29, 28]
        str     x1, [x29, 16]
        ldr     x0, [x29, 16]
        add     x0, x0, 8
        ldr     x0, [x0]
        bl      atoi
        str     w0, [x29, 44]
        ldr     w0, [x29, 44]
        bl      func
        cmp     w0, 0
        bne     .L4
        adrp    x0, .LC0
        add     x0, x0, :lo12:.LC0
        bl      puts
        b       .L6
.L4:
        adrp    x0, .LC1
        add     x0, x0, :lo12:.LC1
        bl      puts
.L6:
        nop
        ldp     x29, x30, [sp], 48
        ret
        .size   main, .-main
        .ident  "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
        .section        .note.GNU-stack,"",@progbits
satwik@Satwik:~/revpico$ code .
```

I opened up the code in VSC for further inspection.

seeing the type, I understood that it had been decompiled from c.

I will try to explain the program now :

So basically in the main function we are giving our argument and then the function is run which stores `7 79 and 3` in memory locations and 1st we do `lsl` operation on `7 and 79` i.e we multiply `79 with 2^7` and we get `10112` as the answer and we store it in a diff memory location then we do `sdiv` on `10112` and `3` where `10112` is dividend and `3` is divisor and we get `3370`. Now we do a `sub` subtraction operation with `3370` and our argument which as we can see in the main function shld make `w0 = 0` so our argument must be `3370`.

In the main function, If `w0=0` after func is run, then we run `lc0` and  get `win` or else lco1 is run which is `lose`.

So converting 3370 to hex = `0D2A`

So flag will be = `picoCTF{00000d2a}`

My commented code which explains what happens in the code way way better :


```
	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 79 ; w0=79
	str	w0, [sp, 16];stores 79 in the sp+16
	mov	w0, 7
	str	w0, [sp, 20];stores 7 in sp+20
	mov	w0, 3
	str	w0, [sp, 24];stores 3 in sp+24
	ldr	w0, [sp, 20] ;argv1=7
	ldr	w1, [sp, 16] ;argv2=79
	lsl	w0, w1, w0 ;lsl is left shift and arguments mean shift w1 by w0 and store in w0 so basically w0=10112
	str	w0, [sp, 28];now we sotring that value in sp+28
	ldr	w1, [sp, 28];loading new args i.e arg1=10112
	ldr	w0, [sp, 24];arg2=3
	sdiv	w0, w1, w0 ; w0 is storage arg, w1 is numerator dividend and w0 is divisor; w0=3370
	str	w0, [sp, 28];string 3370 in sp+28
	ldr	w1, [sp, 28]; w1=3370
	ldr	w0, [sp, 12];w0 = my argument that we give
	sub	w0, w1, w0 ; so w1-w0 = 3370 - myarg = 3370 -3370 for 0
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret  # then we return the value of w0
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16] # what we need starts from here.
	add	x0, x0, 8 # adding 8 to the register which is basically the width of a pointer so were going to argv[1]
	ldr	x0, [x0]
	bl	atoi # ascii to integer
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func # func 1 is called with maybe 1st or second
	cmp	w0, 0 ;to get u win we need w0 to be 0
	bne	.L4 ;to run u lose function if w0 != 0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0 
	bl	puts ; runs .lc0 and gives u win if argument is crct i.e w0 becomes 0
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

![alt text](/PicoCTF/imagesforrev/finish.png)


## Vault Door 3

We are given a Java file, Opening it up in VSC we see

```
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}
```
 Lets ignore the main function for now as it just takes input from user.

 The boolean fucntion rearranges the given password and checks if its equal to a predetermined rearranged password so I just fed the given rearranged password back into the "scrambler". I wrote the code in cpp.

 ```
 #include<iostream>
using namespace std;
int main()
{ 
    string password="jU5t_a_sna_3lpm18g947_u_4_m9r54f";
    char buffer[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password[i];
        }
        for (; i<16; i++) {
            buffer[i] = password[23-i];
        }
        for (; i<32; i+=2) {
            buffer[i] = password[46-i];
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password[i];
        }
        cout<<buffer;
}
```
I got this output after i ran the code :

```
jU5t_a_s1mpl3_an4gr4m_4_u_79958f
```

Then I converted it into a flag : `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}` which was correct.

![alt text](/PicoCTF/imagesforrev/cmpletionofvaultdoor.png)

## ASCII FTW

Downloaded the file using `wgets` changed perms and ran it using `./` and it said the flag starts with 70 and when u convert it to ascii using an online convertor we get `p` then I used gdb to disassemble to disassemble main and input the hex values that are being moved into mem addresses into the online convertor to get the flag.

```

satwik@Satwik:~/picoctf/rev/asciiftw$ file asciiftw
asciiftw: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e1c32dace8ac1516160b771e493f5ebffcac9855, for GNU/Linux 3.2.0, not stripped
satwik@Satwik:~/picoctf/rev/asciiftw$ gdb asciiftw
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
Reading symbols from asciiftw...
(No debugging symbols found in asciiftw)
(gdb) disassemble
No frame selected.
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001169 <+0>:     endbr64
   0x000000000000116d <+4>:     push   %rbp
   0x000000000000116e <+5>:     mov    %rsp,%rbp
   0x0000000000001171 <+8>:     sub    $0x30,%rsp
   0x0000000000001175 <+12>:    mov    %fs:0x28,%rax
   0x000000000000117e <+21>:    mov    %rax,-0x8(%rbp)
   0x0000000000001182 <+25>:    xor    %eax,%eax
   0x0000000000001184 <+27>:    movb   $0x70,-0x30(%rbp)
   0x0000000000001188 <+31>:    movb   $0x69,-0x2f(%rbp)
   0x000000000000118c <+35>:    movb   $0x63,-0x2e(%rbp)
   0x0000000000001190 <+39>:    movb   $0x6f,-0x2d(%rbp)
   0x0000000000001194 <+43>:    movb   $0x43,-0x2c(%rbp)
   0x0000000000001198 <+47>:    movb   $0x54,-0x2b(%rbp)
   0x000000000000119c <+51>:    movb   $0x46,-0x2a(%rbp)
   0x00000000000011a0 <+55>:    movb   $0x7b,-0x29(%rbp)
   0x00000000000011a4 <+59>:    movb   $0x41,-0x28(%rbp)
   0x00000000000011a8 <+63>:    movb   $0x53,-0x27(%rbp)
   0x00000000000011ac <+67>:    movb   $0x43,-0x26(%rbp)
   0x00000000000011b0 <+71>:    movb   $0x49,-0x25(%rbp)
   0x00000000000011b4 <+75>:    movb   $0x49,-0x24(%rbp)
   0x00000000000011b8 <+79>:    movb   $0x5f,-0x23(%rbp)
   0x00000000000011bc <+83>:    movb   $0x49,-0x22(%rbp)
   0x00000000000011c0 <+87>:    movb   $0x53,-0x21(%rbp)
   0x00000000000011c4 <+91>:    movb   $0x5f,-0x20(%rbp)
   0x00000000000011c8 <+95>:    movb   $0x45,-0x1f(%rbp)
   0x00000000000011cc <+99>:    movb   $0x41,-0x1e(%rbp)
   0x00000000000011d0 <+103>:   movb   $0x53,-0x1d(%rbp)
   0x00000000000011d4 <+107>:   movb   $0x59,-0x1c(%rbp)
   0x00000000000011d8 <+111>:   movb   $0x5f,-0x1b(%rbp)
   0x00000000000011dc <+115>:   movb   $0x38,-0x1a(%rbp)
   0x00000000000011e0 <+119>:   movb   $0x39,-0x19(%rbp)
   0x00000000000011e4 <+123>:   movb   $0x36,-0x18(%rbp)
   0x00000000000011e8 <+127>:   movb   $0x30,-0x17(%rbp)
   0x00000000000011ec <+131>:   movb   $0x46,-0x16(%rbp)
   0x00000000000011f0 <+135>:   movb   $0x30,-0x15(%rbp)
   0x00000000000011f4 <+139>:   movb   $0x41,-0x14(%rbp)
   0x00000000000011f8 <+143>:   movb   $0x46,-0x13(%rbp)
   0x00000000000011fc <+147>:   movb   $0x7d,-0x12(%rbp)
   0x0000000000001200 <+151>:   movzbl -0x30(%rbp),%eax

   ```

   ![alt text](/assets/revchoice.png)

   The flag : `picoCTF{ASCII_IS_EASY_8960F0AF}`

# END

