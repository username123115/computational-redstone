def permutate(l, p):
    return [l[i - 1] for i in p]

def p8(x):
    return [(x >> (7 - i)) & 1 for i in range(8)]

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

# Indexed directly by 4-bit input (0000 through 1111)
S0 = [
    0b01, 0b11, 0b00, 0b10,
    0b11, 0b01, 0b10, 0b00,
    0b00, 0b11, 0b10, 0b01,
    0b01, 0b11, 0b11, 0b10,
]

S1 = [
    0b00, 0b10, 0b01, 0b11,
    0b10, 0b00, 0b00, 0b11,
    0b11, 0b10, 0b00, 0b01,
    0b01, 0b01, 0b11, 0b10,
]

IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

def sbox(x, table):
    index = (x[0] << 3) | (x[1] << 2) | (x[2] << 1) | x[3]
    value = table[index]
    return [(value >> 1) & 1, value & 1]

def feistel_round(block, key):
    L, R = block[:4], block[4:]

    print(f"block: {block}")

    expanded = permutate(R, EP)
    print(f"expanded: {expanded}")

    mixed = xor(expanded, key)
    print(f"mixed: {mixed}")

    x, y = mixed[:4], mixed[4:]
    substituted = sbox(x, S0) + sbox(y, S1)
    print(f"substituted: {substituted}")

    f = permutate(substituted, P4)
    print(f"permutated: {f}")

    print(f"xor {L} {f}")

    print(f"R: {R}")
    return xor(L, f) + R

def swap(block):
    return block[4:] + block[:4]

def encrypt(plaintext, k1, k2):
    x = permutate(plaintext, IP)
    x = feistel_round(x, k1)
    x = swap(x)
    x = feistel_round(x, k2)
    return permutate(x, IP_INV)

#print(feistel_round([1, 0] * 4, [1, 0] * 4))
#print(encrypt([0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0]))

stuff = []
k1 = [0, 0, 0, 1, 0, 0, 0, 1]
k2 = [0, 0, 1, 1, 0, 0, 0, 0]

raw = "01100010 01100011 01110100 01100110 01111011 00110001 00110010 01011111 01000010 01001001 01101100 01001100 01101001 01001111 01001110 00101101 01110010 01100101 01110000 01000101 01000001 01010100 01100101 01010010 01110011 01011111 01101100 01100001 01010100 00110011 01110010 01111101".split(" ")



pt = "bctf{12_BIlLiON-repEATeRs_laT3r}"
def encrypt_char(c):
    print(ord(c))
    r = encrypt(p8(ord(c)), k1, k2)
    ct = "".join([str(x) for x in r])
    return ct

print(encrypt_char(pt[17]))
#print(encrypt_char('O'))

"""
ct = []

for c in pt:
    ct.append(encrypt_char(c))

for x in ct:
    print(x)

"""

