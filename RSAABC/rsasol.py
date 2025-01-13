
# Solved : 14 Dec 2024


from Crypto.Util.number import *
from sympy import nextprime, prevprime
import string

# Opening out.txt and getting the encrypted msg, ct and n
f = open("out.txt", "r", encoding="utf=8").read().split("\n")
cipher = f[0]
ct = eval(f'[{f[2]}]')
ns = eval(f'[{f[4]}]')

# translation
language = {
    'A': 'Α', 'a': 'α',
    'B': 'Β', 'b': 'β',
    'C': 'Σ', 'c': 'σ',
    'D': 'Δ', 'd': 'δ',
    'E': 'Ε', 'e': 'ε',
    'F': 'Φ', 'f': 'φ',
    'G': 'Γ', 'g': 'γ',
    'H': 'Η', 'h': 'η',
    'I': 'Ι', 'i': 'ι',
    'J': 'Ξ', 'j': 'ξ',
    'K': 'Κ', 'k': 'κ',
    'L': 'Λ', 'l': 'λ',
    'M': 'Μ', 'm': 'μ',
    'N': 'Ν', 'n': 'ν',
    'O': 'Ο', 'o': 'ο',
    'P': 'Π', 'p': 'π',
    'Q': 'Θ', 'q': 'θ',
    'R': 'Ρ', 'r': 'ρ',
    'S': 'Σ', 's': 'ς',  
    'T': 'Τ', 't': 'τ',
    'U': 'Υ', 'u': 'υ',
    'V': 'Ω', 'v': 'ω',
    'W': 'Ψ', 'w': 'ψ',
    'X': 'Χ', 'x': 'χ',
    'Y': 'Υ', 'y': 'υ',
    'Z': 'Ζ', 'z': 'ζ'
}

# reversing func for non prime ascii values
def reverse_alphabet(char):
    if char.isupper():  
        return chr(155 - ord(char))  
    elif char.islower():  
        return chr(219 - ord(char)) 
    elif(char=='_' or '{' or '}'):
        return 'e'

s = string.ascii_letters

# non prime ascii's value reversed flag part
flag_partial = ""
index_lan = []
for i, char in enumerate(cipher):
    if char == "e":
        flag_partial += "{" if i < 5 else "}" if i == len(cipher) - 1 else "_"
    elif 64 < ord(char) < 91:
        flag_partial += chr(155 - ord(char))
    elif 96 < ord(char) < 123:
        flag_partial += chr(219 - ord(char))
    else:
        index_lan.append(i)
        flag_partial += " "

# translated characters retrived
engs = []
for ix in index_lan:
    for key, value in language.items():
        if cipher[ix] == value:
            engs.append(key)

indexed_eng = list(zip(index_lan, engs))

primeChars = [] # prime ascii value characters
pres = []       # pre for the prime bites
for char in s:
    if isPrime(ord(char)):
        primeChars.append(char)
        mod = ord(char) % 26
        pres.append(mod)

def googly_rev(number, position):
    mask = 1 << position
    return number ^ mask


flag = list(flag_partial)
for index, eng in indexed_eng:
    ciphertext_new = ct[index]
    n = ns[index]
    e = 65537
    for pre in pres:
        if pre < 5:
            pre += 5
        p = nextprime(1 << (pre - 1))
        lim = prevprime(1 << pre)
        while p <= lim:
            if n % p == 0:
                q = n // p
                phi_n = (p - 1) * (q - 1)
                d = pow(e, -1, phi_n)
                for bit_length in range(1020, 1180):    # bruteforcing bit_length for the old ciphertext
                    ciphertext_old = googly_rev(ciphertext_new, bit_length - ord(eng))
                    m = pow(ciphertext_old, d, n)
                    msg = long_to_bytes(m)
                    try:
                        flag[index] = msg.decode()
                        print(''.join(i for i in flag))
                        break
                    except UnicodeDecodeError:
                        p = nextprime(p)
            else:
                p = nextprime(p)

# concatenating the flag parts
flag = ''.join(i for i in flag)
print(f'Flag : {flag}')
# nite{quICklY_grab_the_codE5_sgOqkA}


