numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 1000000000
th = 0
import sys


def is_lex(num):
    return sorted(list(str(num))) == numbers


# def rec(depth, n):
#     if n <= depth:
#         print(n)
#         rec(depth, n + 1)



def gen_nums(m):
    n = []
    while m <= 9:
        n.append(m)
        m += 1
    return n


nums = gen_nums(0)
count = 0
num = [None] * 9

def rec(nums, num, depth, maximum, count, backwords=False):
    if backwords:
        nums.append(num[depth])
        nums.append(num[depth - 1])
        nums.append(num[depth - 2])
        rec(nums, num, depth - 2, maximum, count)
    if depth >= maximum:
        count += 1
        print(count, num)
        if count % 1000 == 0:
            print("At %s" % count)
        if count == 100:
            print("Count 1 000 000: Number = %s" % (''.join(map(str, num))))
            sys.exit("Count 1 000 000: Number = %s" % (''.join(map(str, num))))
        nums.append(num[depth - 1])
        rec(nums, num, depth - 1, maximum, count, backwords=True)

    for num[depth] in nums:
        nums.remove(num[depth])
        rec(nums, num, depth + 1, maximum, count)
    return nums, num, depth, maximum, count


print(nums)
print(rec(nums, num, 0, 9, count))

# print(rec(9, 0))
# print(numbers)
# for num[0] in numbers:
#     numbers.remove(num[0])
#     for num[1] in numbers:
#         numbers.remove(num[1])
#         for num[2] in numbers:
#             numbers.remove(num[2])
#             for num[3] in numbers:
#                 numbers.remove(num[3])
#                 for num[4] in numbers:
#                     numbers.remove(num[4])
#                     for num[5] in numbers:
#                         numbers.remove(num[5])
#                         for num[6] in numbers:
#                             numbers.remove(num[6])
#                             for num[7] in numbers:
#                                 numbers.remove(num[7])
#                                 for num[8] in numbers:
#                                     numbers.remove(num[8])
#                                     for num[9] in numbers:
#                                         count += 1
#                                         if count == 1000000:
#                                             print("Count 1 000 000: Number = %s" % (''.join(map(str, num))))
#                                         print(''.join(map(str, num)))
#                                     numbers.append(num[8])
#                                 numbers.append(num[7])
#                             numbers.append(num[6])
#                         numbers.append(num[5])
#                     numbers.append(num[4])
#                 numbers.append(num[3])
#             numbers.append(num[2])
#         numbers.append(num[1])
#     numbers.append(num[0])
