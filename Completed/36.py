total = 0


def binary(n):
    return "{0:b}".format(n)


def reverse(a):
    return list(reversed(a))


for i in range(1, 1000000):
    l = list(str(i))
    if l == reverse(l):
        bin = list(binary(i))
        if bin == reverse(bin):
            total += i

print("Double Palindromes under 1 000 000: " + str(total))
# Answer: 872187
