def p(n):
    return int(n * (3 * n - 1) / 2)


# print(p(7))


def generate_pents(m):
    a = []
    for i in range(0, m + 1):
        a.append(p(i))
    return a


maximum = 10000
a = generate_pents(maximum)
# print(a)
count = 0
d = []
for j in a:
    if j == 0:
        continue
    if count % 1 == 0:
        print("At %sth j" % count)
    for k in a[count:]:
        if k == j or k == 0:
            continue
        if j + k in a:
            D = abs(j - k)
            if D in a:
                d.append(D)
                print("Double Pent: (%s, %s), D = %s" % (j, k, D))
    count += 1

print("d[] = %s" % d)
# Answer: 5482660
