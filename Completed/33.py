fir = 0
sec = 1
total = 0
fractions = []


def gcd(x, y):
    xarr = []
    yarr = []
    for i in range(1, x + 1 if x > y else y + 1):
        if x % i == 0:
            xarr.append(i)
        if y % i == 0:
            yarr.append(i)
    for i in reversed(xarr):
        if i in yarr:
            return i


def reduce(x, y):
    i = gcd(x, y)
    return int(x / i), int(y / i)


def fir(x):
    return int(x[0])


def sec(x):
    return int(x[1])


for n in range(10, 100):
    if n % 11 == 0:
        continue
    for d in range(n + 1, 100):
        f = n / d
        num = list(str(n))
        den = list(str(d))
        if sec(den) != 0:
            if sec(num) == fir(den):
                if fir(num) / sec(den) == f:
                    fractions.append([n, d])


def final(fracs):
    num = 1
    den = 1
    nums = []
    dens = []
    for frac in fractions:
        nums.append(frac[0])
        dens.append(frac[1])
    for i in nums:
        num *= i
    for i in dens:
        den *= i

    val = reduce(num, den)
    return val[1]


print("Total: %i" % total)
print("Fractions: %a" % fractions)
print("Final: %i" % final(fractions))
# Answer: 100
