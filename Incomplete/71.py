from Scripts import is_prime


def hcf(x, y):
    # Use primes
    # TODO: Optimize
    xs = [x] if x == 1 else []
    if x in primes:
        xs = [1, x]
    else:
        for i in range(1, x + 1):
            if x % i == 0:
                xs.append(i)
    for i in reversed(xs):
        if y % i == 0:
            return i

    # a, b = min(x, y), max(x, y)
    # a1 = []
    # for i in reversed(range(1, a + 1)):
    #     if a % i == 0:
    #         if b % i == 0:
    #             return i


def sort(arr):
    index = 0
    d = dict()
    for frac in arr:
        d[frac[0] / frac[1]] = frac
        index += 1
    new_arr = []
    for key in sorted(d.keys()):
        new_arr.append(d[key])
    return new_arr


def get_primes():
    primes = []
    for i in range(1, 1000000):
        if i % 100000 == 0:
            print("At i = %s" % i)
        if is_prime(i):
            primes.append(i)
    print("primes", primes)
    return primes


primes = get_primes()
l = 1000000
fractions = []

for d in range(1, l + 1):
    if d % 100 == 0:
        print("At d = %s" % d)
    for n in range(1, d):
        if hcf(n, d) == 1:
            fractions.append([n, d])

fractions = sort(fractions)
index_of_3_7 = fractions.index([3, 7])
frac = fractions[index_of_3_7 - 1]
print("Fraction: %s, Answer: %s" % (frac, frac[0]))
