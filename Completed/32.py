from Scripts import is_pandigital

count = 0
skip = False
for prod in range(1, 10000):
    skip = False
    if prod % 100 == 0:
        print("At %s" % prod)
    for a in range(1, prod + 1):
        if skip:
            break
        for b in range(a, prod):
            if skip:
                break
            if a * b == prod:
                if is_pandigital(str(a) + str(b) + str(prod)):
                    print("%s = %s x %s" % (prod, a, b))
                    count += prod
                    print("Count = %s" % count)
                    skip = True

# Answer: 45228