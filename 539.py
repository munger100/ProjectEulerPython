pairs = {}


def p(n):
    l = []
    [l.append(i) for i in range(1, n + 1)]
    while len(l) > 1:
        x = []
        [x.append(a) for a in range(0, len(l), 2)]
        for a in sorted(x, reverse=True):
            del l[a]
        if len(l) > 1:
            y = []
            [y.append(b) for b in range(len(l) - 1, -1, -2)]
            for b in sorted(y, reverse=True):
                del l[b]
    return l[0]


def s(n):
    total = 0
    a = 1
    b = n
    for x in range(a, b + 1):
        if x % 1000 == 0:
            print("At %s on %s, %s left" % (x, n, n - x))
        total += p(x)
    return total


t = 10
for a in range(1, 19):
    t *= 10
z = t

print("P(%s) = %s" % (z, s(z)))
