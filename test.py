# num = 10000
# total = 300000
# print(num * 100 / total)

# num = [1, 5, 6, 3, 6, 8]
# print("Count 1 000 000: Number = %s" % (''.join(map(str, num))))

# print(1/7)

# arr = [1, 5, 10, 15, 20]
#
# for a in arr:
#     print(arr)
# print(arr)
# arr[arr.index(a)] = a + 1
# print(a)
# arr[-1] = 0
#
# print(arr)

# a = "asdasds"
# b = list(a)
# print(a)
# print(b)
# print(''.join(b))


def is_pandigital(n):
    n = str(n)
    for i in range(1, len(n) + 1):
        if str(i) not in n:
            return False
    return True


# print(is_pandigital(999999999))

from Scripts import is_prime
import time


def is_cyclic(n):  # n must be str
    n = str(n)
    m = len(n)
    init = n = list(n)
    while n[0] == "0":
        del n[0]
    n = int(''.join(n))
    # print("init(n) == %s" % init)
    cyc = True
    for i in range(2, m):
        x = n * i
        init_temp = list(str(x))
        # print("init_temp) == %s" % init_temp)
        y = init_temp
        y.append(y.pop(0))
        a = False
        for i in range(1, len(y)):
            if y == init:
                a = True
                # print(y)
                break
            y.append(y.pop(0))
        if not a:
            cyc = False
            # print(y)
    return cyc


# limit = 100000000
# pt = 0
# ct = 0
# for i in range(1, limit):
#     if i % 100000 == 0:
#         print("i = %s" % i)
#     a = time.time()
#     is_prime(i)
#     b = time.time()
#     prime = b - a
#     print("is_prime(%s): %s seconds" % (i, prime))
    # is_cyclic(i)
    # c = time.time()
    # cycle = c - b
    # print("is_cyclic(%s): %s seconds" % (i, cycle))
    # print("Fastest: %s" % ("cycle" if prime > cycle else "prime"))
    # pt += 1 if cycle > prime else 0
    # ct += 1 if cycle < prime else 0

# print("pt, ct = %s, %s" % (pt, ct))

# Gotta get better exceptions, maybe prime iirc. In test.py i tried it and primes are faster than cyclics 80% of time