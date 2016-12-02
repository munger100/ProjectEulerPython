from Scripts import is_prime

limit = 1000000
primes = []
highest = [0.0]


def find_consecs(n, p, h):
    arr = []
    for i in range(0, len(p)):
        c = 0
        j = 0
        while c < n:
            c += p[i + j]
            j += 1
            # print("c = %s" % c)
            if c == n:
                # print("Yay %s, %s" % (n, j))
                if j > h[0]:
                    h = [j, n]
                arr.append([n, j])
            if c > n:
                break
    return h

    # WAT


for i in range(1, limit):
    if i % 10000 == 0:
        print("i = %s" % i)
    if is_prime(i):
        primes.append(i)
    else:
        continue
    highest = find_consecs(i, primes, highest)

print("[Highest seq, Highest num] = %s" % highest)

# Answer: 997651