# Reverse Engineering
In this Writeup, we learn how to decompile and understand waht happens under the hood when we run files and how to exploit them to get our flags.
## GDB baby step 1
 I saw the 2 videos by low level code on how to try to infer information from the decompiled assembly code and understood how that in the main function the contents of `86342h` is being stored in `eax`.

 ![ida main file](/PicoCTF/imagesforrev/image.png)