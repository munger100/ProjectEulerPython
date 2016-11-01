from Sources.Scripts import is_prime

limit = 1000000


def next_perm(n):
    i = list(str(n))
    i.insert(0, i.pop(-1))
    return int(to_str(i))


def to_str(a):
    if a is int:
        return str(a)
    if a is not str:
        return ''.join(a)
    return str(a)


count = 1  # to account for 2, which is skipped with interval
ice = [2, 4, 6, 8, 0]

for i in range(1, limit, 2):
    for e in ice:
        if e in list(str(i)):
            break
    k = i
    if is_prime(k):
        if len(str(k)) == 1:
            print(i)
            count += 1
            continue
        for j in range(1, len(str(k))):
            k = next_perm(k)
            if not is_prime(k):
                break
            if j == len(str(i)) - 1:
                count += 1
                print("%s %sth" % (i, j))

print("Count = %s" % count)

# Answer: 55
