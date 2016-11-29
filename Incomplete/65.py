from fractions import Fraction
from decimal import Decimal


# 5       |   74
# ________| 0.067
# - 4.44, 74*(5/74) First Digit
# = .56(0)
# - .518, 74*(560/74) FD
# = .42
# - .370, 74*(420/74) FD
# = .05

# Get leading nums, excluding 0s to check for remainder repitition
# Keep count of remainders for repeats
# Append 0s to num if dont fit, except on first z


def get_first(n, mode):
    arr = []
    for char in str(n):
        if char == '.':
            arr.append(char)
        elif int(char) == 0:
            arr.append(char)
        else:
            arr.append(char)
            break
    if mode == 1:  # Full
        return ''.join(arr)
    if mode == 2:  # First actual int
        return arr[-1]
    return None


def long_division(a, b):
    # a/b
    arr = []
    rems = [a]
    init = a / b
    print(init)

    first = get_first(init, 1)
    quotient = [list(first)]
    print(first)

    rem = a - b * Decimal(first)

    while rem not in rems:
        print("butts")
        rems.append(rem)
        while Decimal(rem) < b:
            while Decimal(rem) < 1:
                rem *= 10
            print("balls")
            print(rem)
            rem = str(rem) + str(0)
        rem = Decimal(rem - b * int(get_first(rem / 74, 2)))
        print(rem)
    print(rem)

    # put all > 1, remove .,

    return arr


print(long_division(5, 74))

# def gen_e(start, length):
#     arr = [start]
#     for i in range(1, length):
#         arr.append([1, start * i, 1])
#     return arr
#
#
# e = gen_e(start=2, length=10)
#
# sequence = []
#
#
# def get_nth_convergent(n):
#     start = e[0]
#     nums = []
#     for i in range(1, n - 1):
#         nums.append(e[i][1])
#     num = iterate(nums, n, n, start, start)
#     return Fraction(num)
#
#
# def iterate(nums, length, base, start, num):
#     if length > 0:
#         num = num / iterate(nums, length - 1, base, start, num)
#     return num
# print(Fraction(1 + (1/(2 + 1/(2)))))
#
#
# print(get_nth_convergent(10))
#
# print(Fraction(2 + 1 / (2 + 1 / (2))))
# print(Fraction(str(1 + 1 / (2 + 1 / (2)))))
# print(Fraction(str(1 + 1 / (2 + 1 / (2 + 1 / (2))))))
# print((str(1 + 1 / (2 + 1 / (2)))))
#
# print(sequence[100 - 1])
#
#
# Problem: fkin repeating decimals
#
