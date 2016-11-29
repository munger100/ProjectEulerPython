limit = 1000000000
import math
total = 0

def area(a, b, c):
    h = math.sqrt(a ** 2 - (b / 2) ** 2)
    return b * h / 2


for a in range(1, 555000000):
    if a % 1000000 == 0:
        print("At %s" % a)
        print("Total = %s" % total)
    b = a
    c = a - 1
    p = a + b + c
    A = area(a, c, b)
    if p % 1 == 0 and A % 1 == 0:
        # print("Both integral, %s, %s, %s" % (a,b,c))
        if p < limit:
            total += p
        else:
            print("Nope")
            break
    c = a + 1
    p = a + b + c
    A = area(a, c, b)
    if p % 1 == 0 and A % 1 == 0:
        # print("Both integral, %s, %s, %s" % (a,b,c))
        if p < limit:
            total += p

print("total = %s" % total)
