___author___ = "Matthew"

highest = [0, 0]
for num in range(3, 1000000):
    if num % 10000 == 0:
        print("At: %s" % num)
    terms = 0
    n = num
    while int(n) is not 1:
        terms += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    if terms > highest[0]:
        highest[0] = terms
        highest[1] = num

print("Longest Sequence: %s, Starting Number: %s" % (highest[0], highest[1]))

# Answer: Longest Sequence: 524, Starting Number: 837799
