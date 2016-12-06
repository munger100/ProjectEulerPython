from Scripts import is_prime


def is_pandigital(n):
    n = str(n)
    if len(n) == 10:
        for i in range(0, 10):
            if str(i) not in n:
                return False
        return True
    return False


primes = []
start = 999999999
limit = 10000000000
# start = 1406357289
total = 0

for i in range(1, 18):
    if is_prime(i):
        primes.append(i)
print(primes)

for i in range(start, limit):
    if i % 1000000 == 0:
        print("i = %s" % i)
    if is_pandigital(i):
        # print("pan " + str(i))
        for j in range(0, len(primes)):
            arr = []
            d = j + 2
            for x in range(0, 3):
                # print(x, d)
                arr.append(str(i)[d + x - 1])
            a = int(''.join(arr))
            if a / primes[j] % 1 == 0:
                # print("ya")
                if j == len(primes) - 1:
                    print("WORKS")
                    total += i
            else:
                break

print("Total = %s" % total)

# Answer: 16695334890