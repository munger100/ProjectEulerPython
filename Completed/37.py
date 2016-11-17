from Scripts import is_prime

v = 71933
primes = []
limit = 1000000
total = 0
count = 0
for i in range(1, limit):
    print("i = %s" % i) if i % 100000 == 0 else None
    temp = str(i)
    forwards = False
    backwards = False
    if is_prime(i):
        primes.append(i)
        if i < 10:
            continue
        while len(temp) > 1:
            if v == i:
                print("Temp = %s" % temp)
            temp = temp[:-1]
            # print("Temp = %s" % i)
            if int(temp) in primes:
                continue
            break
        if len(temp) == 1:
            if int(temp) in primes:
                forwards = True
                # print("%s is forw trunc prime" % i)
        temp = str(i)
        while len(temp) > 1:
            if v == i:
                print("Temp = %s" % temp)
            temp = temp[1:]
            # print("Temp = %s" % i)
            if int(temp) in primes:
                continue
            break
        if len(temp) == 1:
            if int(temp) in primes:
                backwards = True
                # print("%s is back trunc prime" % i)
    if forwards and backwards:
        print("%s is fully truncatable prime!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % i)
        count += 1
        total += i

print("Count = %s" % count)
print("Total = %s" % total)

# Answer: 748317
