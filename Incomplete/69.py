from Sources import scripts

val = 0
divisors = []


def gcd(x, y):
    # print(divisors)
    greatest = 0
    a = divisors[x - 1]
    b = divisors[y - 1]
    # print(x, a, y, b)
    for i in a:
        if i in b:
            greatest = i if i > greatest else greatest
    return greatest


def phy(num):
    count = 0
    for i in range(1, num + 1):
        if len(divisors) < i:
            divisors.append(scripts.get_divisors(i))
            # print(num, i, divisors)
    for i in range(1, num):
        if gcd(i, num) == 1:
            count += 1
    return count


def n_of_phy(num):
    p = phy(num)
    return num / p if p != 0 else 0


def get_maximum(m):
    maximum = [0, 0]
    for n in range(2, m + 1):
        if n % 1000 == 0:
            print("At %s of %s" % (n, m))
        nop = n_of_phy(n)
        if nop > maximum[0]:
            maximum[0] = nop
            maximum[1] = n
    return maximum


print("phy of 9 = " + str(phy(9)))
print("phy of 10 = " + str(phy(10)))
print(get_maximum(10))
print(divisors)
# print(n_of_phy(10))
# print(divisors)
print(get_maximum(1000000))

# Gotta check gcd as it goes  instead of compiling them on