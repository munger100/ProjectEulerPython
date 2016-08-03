# ord(n) = ASCII value of n
# chr(n) = Char of ASCII VALUE n
with open("../Sources/59 XOR decryption.txt") as f:
    data = f.read().strip()
import string

cypher = data.split(",")
lwc = list(string.ascii_lowercase)
words = ["and", "the", "or", "it", "if"]


def get_ascii(n):
    return ord(n)


def get_chr(n):
    return chr(n)


def decipher(x, y, z, cypher):
    r = [x, y, z]
    l = []
    i = 0
    while len(l) < len(cypher):
        l.append(r[i % 3])
        i += 1
    # print("l = %s" % l)
    message = []

    for i in range(0, len(cypher)):
        c = int(cypher[i])
        a = get_ascii(l[i])
        if c > a * 2:
            message.append(c - a)
        elif a > c * 2:
            message.append(a - c)

    m = []
    for integer in message:
        m.append(get_chr(integer))
    # print(m)
    m = "".join(m)
    return m


for a in lwc:
    print("At %s on %s" % (a, lwc[-1]))
    for b in lwc:
        for c in lwc:
            d = decipher(a, b, c, cypher)
            e = d.split(" ")
            for word in words:
                if word in e:
                    print(word)
                    print(d)
