# Cryptography

## C3
### Thought process:

Firstly I downloaded `ciphertext` and `convert` from the website using wgets.

On inspecting the files using VSCODE, I found that `convert` is a python script that acts as a encoder and `ciphertext` is the encoded message.I tried reversing the things that `convert` does and wrote a `decoder.py` script.

```
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

for char in chars:
 cur = lookup2.index(char)
 out += lookup1[(cur + prev) % 40]
 prev = (cur+prev) % 40

sys.stdout.write(out)
 
```

I ran the script passing in `ciphertext` as the input and it gave me the following code snippet:

```
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
```

I tried to run this python script but it had a syntax error so I corrected it enclosing the print command with brackets:
```
- print chars[o] #prints
+ print(chars[0]) #prints
```
Initially I tried passing in `ciphertext` as the input for the script but it was not correct and then I tried passing in the script itself as the input and it printed out the following which turned out to be the flag.
```
a
d
l
i
b
s
```


### Concepts Used

- Learnt basics of python syntax and how the `fileinput` package works.
- Learnt how to reverse ciphers.

### Incorect tangents 

After getting the decoded script, I ran the script passing in `ciphertext` as the input but I didnt get the flag.


 I was stuck on this from a long time. Then I read the comments of script and noticed `#selfinput` so I passed the program itself as the text to be decoded and it worked.

### The FLAG

Following the picoCTF flag format I got the flag:

```
picoCTF{adlibs}
```
![alt text](/PicoCTF/imagesforrev/finishc3.png)

## Custom Encryption

The name suggests the encryption is custom (KEK) so let's look at the code for a bit:

```
from random import randint
import sys


def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text


def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')


if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")
```

After a little bit of googling I understood that the text() function basically allows two people to derive a shared secret key without directly transmitting it.

* p and g are predefined constants representing a prime modulus and a base
* Random integers a and b are generated as private keys
* A shared secret key (key or b_key) is derived AND if they match we can proceed.
* Next a Xor encryption takes place with the reversed plain text and text_key
* Then in the encrypt() function, we take the xor encrypted string and extract each value's ascii, multiply with key and also multiply with 311.
* The output is a list of integers (cipher), representing the final ciphertext.

To Reverse this ecnryption was not easy but  I started out by trying to convert the encrypted text to semi-encrypted text.

I realized I had to get the shared key values u and v first so i wrote the function `halfdecrypt()` which uses `a,b` provided in the text file and `p,g` is given in the pgm also the ciphertext is provided in the text file. and then to get the half decrypted text I just reversed the process using `decrypt()` and then doing the xor reversal was hard and I kept getting stuck in Random places but after reversing and xoring 3 times I got the flag finally. 
The program :

```
from random import randint
import sys


def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

def dynamic_xor_decrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)

    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char

    plaintext = cipher_text
    cipher_text = ""

    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char

    plaintext = cipher_text
    cipher_text = ""

    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    
    return cipher_text


def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')

def decrypt(cipher, key):
    plaintext = ""
    for encrypted_value in cipher:
        decrypted_value = encrypted_value // (key * 311)
        plaintext += chr(decrypted_value)
    return plaintext

def halfdecrypt():
    p = 97
    g = 31
    a = 88
    b = 26

    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)

    shared_key = None
    if key == b_key:
        shared_key = key
   
    cipher = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]

    semi_cipher = decrypt(cipher, shared_key)

    flag = dynamic_xor_decrypt(semi_cipher, "trudeau")

    print(flag)


if __name__ == "__main__":
    # message = sys.argv[1]
    # test(message, "trudeau")
    halfdecrypt()
```

The flag : `picoCTF{custom_d2cr0pt6d_019c831c}`

Problems Faced : Since Im unfamiliar with python, It took a long time for me to understand whats going on and also write new code. Also faced problems in `decrypt()` using `/` but learnt about `//` which discards the remained basically removing the `'float' object cannot be interpreted as an integer` error.

## Mini RSA
Since RSA is a Familiar word, I did some reading on it in GFG.
https://www.geeksforgeeks.org/rsa-algorithm-cryptography/

Also went through the hints where I got more info about RSA encryption. 
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

2nd hint : How could having too small an e affect the security of this 2048 bit key?
3rd hint : Make sure you don't lose precision, the numbers are pretty big (besides the e value).

We have been given a very large N : (product of primes) : `29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673`

and a small e (hint) : `3`

The encyrpted text : ` 2205316413931134031074603746928247799030155221252519872650073010782049179856976080512716237308882294226369300412719995904064931819531456392957957122459640736424089744772221933500860936331459280832211445548332429338572369823704784625368933`

Now to decrypt the message, I had to do a lot of research but I understood the math pretty easily, The encryption algorithm is as follows, `c = (M ^ e) % N ` , where c = cipher text, M = main text , e = encryption (public) key , N = part of both public and private key

So if N>>>>e then (M^e) % N == (M^e) but if N < e then we cannot just root inverse it to decrypt, so I reverse the algorithm and find out a way to get the plain text , `M = {(N*i) + c} ^ (1/3)` // where , i = any positive integer. So now I was in a pinch but after going through some websites on how one could possibly decode RSA encryptions, I found this : `https://crypto.stackexchange.com/a/80346` and understood that m^3%N != N thus I developed this python script to decode the answer and used the precision hint to get the full flag.

```
from decimal import *
from tqdm import tqdm

N = Decimal(29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673)
e = Decimal(3)
c = Decimal(2205316413931134031074603746928247799030155221252519872650073010782049179856976080512716237308882294226369300412719995904064931819531456392957957122459640736424089744772221933500860936331459280832211445548332429338572369823704784625368933)


def int_to_ascii(m):
    # Decode to ascii (from https://crypto.stackexchange.com/a/80346)
    m_hex = hex(int(m))[2:-1]  # Number to hex
    m_ascii = "".join(
        chr(int(m_hex[i : i + 2], 16)) for i in range(0, len(m_hex), 2)
    )  # Hex to Ascii
    return m_ascii


# Find padding
getcontext().prec = 280  # Increase precision
padding = 0
for k in tqdm(range(0, 10_000)):
    m = pow(k * N + c, 1 / e)

    m_ascii = int_to_ascii(m)

    if "pico" in m_ascii:
        padding = k
        break

print("Padding: %s" % padding)

# Increase precision further to get entire flag
getcontext().prec = 700

m = pow(padding * N + c, 1 / e)
m_ascii = int_to_ascii(m)
print("Flag: %s" % m_ascii.strip())
```

The Flag :`Flag: picoCTF{n33d_a_lArg3r_e_ccaa7776}`


