def is_pandigital(n):
    n = str(n)
    if len(n) == 9:
        for i in range(1, 10):
            if str(i) not in n:
                return False
        return True
    return False


def to_str(a):
    if a is not str:
        return ''.join(a)
    return str(a)


limit = 1000000
highest = 0

for i in range(1, limit):
    if len(str(i)) > 5:
        print("Reached end")
        break
    p = []
    count = 1
    while len(p) < 10:
        if len(p) == 9:
            if is_pandigital(to_str(p)):
                print("%s works, %s" % (i, p))
                z = int(to_str(p))
                highest = z if z > highest else highest
        entry = count * i
        for j in str(entry):
            p.append(j)
        count += 1
    if i == 192 or i == 9:
        print(p)
    if i % 10000 == 0:
        print(i)

print("Highest = %s" % highest)

# Answer: 932718654
