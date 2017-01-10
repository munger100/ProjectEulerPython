total = 0

for i in range(1, 100):
    l = i
    n = 0
    k = 0
    while len(str(n)) <= l:
        k += 1
        n = k ** i
        if len(str(n)) == l:
            total += 1
            print("%s at %sth power" % (k, i))

print("Total = %s" % total)

# Answer: 49
