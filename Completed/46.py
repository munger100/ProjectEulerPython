def is_composite(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


primes = []
theory = []


def this(i):
    if is_composite(i):
        for p in primes:
            for s in range(1, i - p):
                if p + 2 * (s ** 2) == i:
                    theory.append(i)
                    return None
        return True
    else:
        primes.append(i)


for i in range(3, 50000, 2):
    if i % 101 == 0:
        print("At %s" % i)
    if this(i) == True:
        print("Answer: %s" % i)
        break
    this(i)

# Answer: 5777