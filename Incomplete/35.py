from Sources.Scripts import isPrime

circular_primes = [2]


def get_permutations(n):
    n = str(n)
    arr = list(n)
    if len(n) <= 1:
        return [n]
    perms = [n]
    for i in range(0, len(n) - 1):
        arr.append(arr.pop(0))
        perms.append(''.join(arr))
    perms.remove(str(n))
    return perms


for i in range(3, 1000000, 2):
    if i % 10000 == 0:
        print("At " + str(i))
    if i not in circular_primes:
        if isPrime(i):
            temp = []
            for perm in get_permutations(i):
                if not isPrime(int(perm)):
                    continue
                temp.append(int(perm))
            circular_primes.append(i)
            for t in temp:
                if t not in circular_primes:
                    circular_primes.append(t)

print(circular_primes)
print(len(circular_primes))
