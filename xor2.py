from pwn import xor
s = b"label"
k = 13
r = xor(s,k)
flag = f"crypto{{{r.decode()}}}"
print(flag)

