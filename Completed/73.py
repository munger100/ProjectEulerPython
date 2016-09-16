def hcf(x, y):
    smaller = x if x < y else y
    highest = 1
    for i in range(2, smaller + 1):
        if x % i == 0 and y % i == 0:
            return i
    return highest


def get_list(d):
    small = 1 / 3
    big = 1 / 2
    count = 0
    for y in range(1, d + 1):
        if y % 50 == 0:
            print("Getting y=%s on %s" % (y, d))
        for x in range(1, y):
            if hcf(x, y) == 1:
                quotient = x / y
                if small < quotient and quotient < big:
                    count += 1
    print("Done get_list")
    return count


count = get_list(12000)

print(count)
# Answer: 7295372
