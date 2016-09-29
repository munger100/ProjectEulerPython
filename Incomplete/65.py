from fractions import Fraction
from decimal import Decimal


def gen_e(start, length):
    arr = [start]
    for i in range(1, length):
        arr.append([1, start * i, 1])
    return arr


e = gen_e(start=2, length=10)

sequence = []


def get_nth_convergent(n):
    start = e[0]
    nums = []
    for i in range(1, n - 1):
        nums.append(e[i][1])
    num = iterate(nums, n, n, start, start)
    return Fraction(num)


def iterate(nums, length, base, start, num):
    if length > 0:
        num = num / iterate(nums, length - 1, base, start, num)
    return num


# print(get_nth_convergent(10))

print(Fraction(2 + 1 / (2 + 1 / (2))))

print(Fraction(str(1 + 1 / (2 + 1 / (2)))))
print(Fraction(str(1 + 1 / (2 + 1 / (2 + 1 / (2))))))
print((str(1 + 1 / (2 + 1 / (2)))))

# print(sequence[100 - 1])


# Problem: fkin repeating decimals
