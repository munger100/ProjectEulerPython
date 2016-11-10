from Scripts import is_prime


def is_pandigital(n):
    n = str(n)
    for i in range(1, len(n) + 1):
        if str(i) not in n:
            return False
    return True


highest = 0

limit = 999999999

for i in reversed(range(1, limit, 2)):
    if i % 10000001 == 0:
        print("At %s" % i)
    if is_pandigital(i):
        if is_prime(i):
            print("%s is largest pandigital prime" % i)
            break

# Answer: 7652413
