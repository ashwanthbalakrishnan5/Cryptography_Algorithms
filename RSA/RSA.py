import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def rabin_miller(n, k):
    s = n - 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x in [1, -1]:
            continue
        else:
            return False
    return True


def generate_random_prime(bits):
    while True:
        x = random.randrange(2 ** (bits - 1) + 1, 2**bits - 1, 2)
        if pow(2, x - 1, x) == 1:
            if rabin_miller(x, 40):
                return x


def egcd(a, b, x=0, y=1):
    x, y = y, x - (b // a) * y
    if b % a == 0:
        return x, y
    return egcd(b % a, a, x, y)


def generate_key_pair(bits):

    p, q = generate_random_prime(bits), generate_random_prime(bits)
    print(f"P : {p}\nQ :{q}\n")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = egcd(e, phi)[0]
    if d < 0:
        d += phi
    keys = {
        "p": p,
        "q": q,
        "phi": phi,
        "public": e,
        "private": d,
        "modulus": n,
    }
    return keys


chars = [
    char
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`1234567890-=~!@#$%^&*()_+[]\\{}|;':,./<>? "
]


def encrypt(m, e, n):
    c = []
    for i in range(len(m)):
        c.append(pow(chars.index(m[i]), e, n))
    return "-".join([str(num) for num in c])


def decrypt(c, d, n):
    m = []
    for i in c.split("-"):
        m.append(chars[pow(int(i), d, n)])
    return "".join(m)


key_pair = generate_key_pair(1024)
text = input("Enter the Message:")
cipher = encrypt(text, key_pair["public"], key_pair["modulus"])
print(f"Encrypted Text : {cipher}\n")
decrypted_message = decrypt(cipher, key_pair["private"], key_pair["modulus"])
print(f"Decrypted Text : {decrypted_message}\n")
