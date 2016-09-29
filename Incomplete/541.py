def gcd(a, b):
    t = 0
    high = (a if a > b else b)
    for i in range(1, high + 1):
        t = (i if a % i == 0 and b % i == 0 else t)
    return t


def h(n):
    None
