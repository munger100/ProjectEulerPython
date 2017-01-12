from Scripts import is_prime

primes = []
limit = 200000
l = 4
last = 0
ls = []

for i in range(2, limit):
    if is_prime(i):
        primes.append(i)
        continue
    facts = []
    for p in primes:
        if i % p == 0:
            facts.append(p)
    if i % 10000 == 0:
        print("At %s" % i)
    if len(facts) == l:
        ls.append(i)

print("ls = %s" % ls)

# Gotta find consec in arr ls below
arr = []
for item in ls:
    if len(arr) == l:
        print("Done", arr)
        break
    if len(arr) == 0:
        arr.append(item)
        continue
    else:
        if arr[-1] == item - 1:
            arr.append(item)
        else:
            arr = [item]

print("Answer: %s" % arr[0])
# Answer: 134043
