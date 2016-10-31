from fractions import Fraction


def is_resilient(a, b):
    string = "%s/%s" % (a, b)
    if string == str(Fraction(a, b)):
        return True
    return False


def r(d):
    count = 0
    for i in range(d):
        if is_resilient(i, d):
            count += 1
    return [count, d - 1]


# b = 12
# for a in range(1, b):
#     is_resilient(a, b)
# print(r(12))
maximum = Fraction(0, 1)
top = 1000000
limit = Fraction(15499, 94744)
ans = 892371480
for i in range(ans, ans + 1):
    if i % 1 == 0:
        print("At %s" % i)
    res = r(i)
    print("Done res")
    new = Fraction(res[0], res[1])
    m = maximum
    if new > m:
        if new < limit:
            # maximum = [n, d]
            maximum = new
            print(maximum, i)

greatest = maximum
print(greatest)
