from Sources import scripts

f = scripts.factorial
counter = 0


def C(n, r):
    if n >= r:
        return int(f(n) / (f(r) * f(n - r)))
    else:
        return ValueError


for n in range(1, 100 + 1):
    print("At N = %i" % n)
    for r in range(1, n + 1):
        if C(n, r) > 1000000:
            counter += 1

print(counter)
# Answer: 4075
