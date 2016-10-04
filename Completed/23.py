maximum = 28123
count = 0
abundants = []


def get_divisors(n):
    d = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            d.append(i)
    return d


def is_abundant(n):
    t = 0
    # t += [num for num in get_divisors(n)]
    for num in get_divisors(n):
        t += num
    return t > n


def can_be_sum(n):
    for a in abundants:
        for b in reversed(abundants):
            if a + b == i:
                return True
            else:
                continue
    return False


for i in range(1, maximum + 1):
    print("At %s on %s" % (i, maximum)) if i % 1000 == 0 else None
    abundants.append(i) if is_abundant(i) else None
    if not can_be_sum(i):
        count += i

print("Count: {c}".format(c=count))
print("Abundants: {a}".format(a=abundants))

# Answer: 4179871
