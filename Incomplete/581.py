from Sources.Scripts import is_prime

primes = [1]

def is_p_smooth(p, n):
    for i in range(min(primes[-1], n), int(n) + 1):
        if is_prime(i):
            primes.append(i)
            if n % i == 0:
                if i > p:
                    return False
    return True

def t(n):
    return n*(n+1)/2
total = 0
p = 47
for i in range(1, 10000):
    if i % 100 == 0:
        print("At %s, total = %s" % (i, total) )
    num = t(i)
    p_smooth = is_p_smooth(p, num)
    if p_smooth:
        total += i