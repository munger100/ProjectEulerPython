import math

highest = 0

def sqrt(num):
    return math.sqrt(num)


def square(num):
    return num ** 2


def is_right(a, b, c):
    return square(a) + square(b) == square(c)

for p in range(1, 1001):
    count = 0
    print("Doing " + str(p))
    for int in range(1, p):
        a = int
        for int2 in range(a, p):
            b = int2
            for int3 in range(1, p):
                c = int3
                if is_right(a, b, c) and a + b + c == p:
                    print("{%s, %s, %s}" % (a, b, c))
                    count += 1
    if count > highest:
        highest = count
        value = p
        print("Highest Count: %s, Value to that Count: %s" % (highest, value))
# Answer: 39