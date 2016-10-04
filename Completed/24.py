# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = 1000000000
# th = 0
# import sys
#
#
# def is_lex(num):
#     return sorted(list(str(num))) == numbers
#
#
# def rec(depth, n):
#     if n <= depth:
#         print(n)
#         rec(depth, n + 1)

#
#
# def gen_nums(m):
#     n = []
#     while m <= 9:
#         n.append(m)
#         m += 1
#     return n
#
#
# nums = gen_nums(0)
# count = 0
# num = [None] * 9
#
# def rec(nums, num, depth, maximum, count, backwords=False):
#     if backwords:
#         nums.append(num[depth])
#         nums.append(num[depth - 1])
#         nums.append(num[depth - 2])
#         rec(nums, num, depth - 2, maximum, count)
#     if depth >= maximum:
#         count += 1
#         print(count, num)
#         if count % 1000 == 0:
#             print("At %s" % count)
#         if count == 100:
#             print("Count 1 000 000: Number = %s" % (''.join(map(str, num))))
#             sys.exit("Count 1 000 000: Number = %s" % (''.join(map(str, num))))
#         nums.append(num[depth - 1])
#         rec(nums, num, depth - 1, maximum, count, backwords=True)
#
#     for num[depth] in nums:
#         nums.remove(num[depth])
#         rec(nums, num, depth + 1, maximum, count)
#     return nums, num, depth, maximum, count
#
#
# print(nums)
# print(rec(nums, num, 0, 9, count))
#
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
nums = []
current = []
for i in range(0, 3):
    for j in range(0, 3):
        if j == i:
            continue
        for k in range(0, 3):
            if k == i or k == j:
                continue
            nums.append([i, j, k])
nums = []
limit = 10
for i in range(0, limit):
    print("At i = %s" % i)
    current.append(i)
    for j in range(0, limit):
        if j in current:
            continue
        current.append(j)
        for k in range(0, limit):
            if k in current:
                continue
            current.append(k)
            for l in range(0, limit):
                if l in current:
                    continue
                current.append(l)
                for m in range(0, limit):
                    if m in current:
                        continue
                    current.append(m)
                    for n in range(0, limit):
                        if n in current:
                            continue
                        current.append(n)
                        for o in range(0, limit):
                            if o in current:
                                continue
                            current.append(o)
                            for p in range(0, limit):
                                if p in current:
                                    continue
                                current.append(p)
                                for q in range(0, limit):
                                    if q in current:
                                        continue
                                    current.append(q)
                                    for r in range(0, limit):
                                        if r in current:
                                            continue
                                        nums.append([i, j, k, l, m, n, o, p, q, r])
                                    current.remove(q)
                                current.remove(p)
                            current.remove(o)
                        current.remove(n)
                    current.remove(m)
                current.remove(l)
            current.remove(k)
        current.remove(j)
    current.remove(i)

print("1 000 000th = %s" % nums[999999])
a = map(str, nums[999999])
a = ''.join(a)
print("1 000 000th = %s" % a)



# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers = [0, 1, 2]
# def start(maximum):
#     nums = []
#     for i in numbers:
#
#     return nums
#
def rec(nums, num, maximum, length):
    print("New rec, nums = %s, num = %s" % (nums, num))
    for i in range(0, maximum + 1):
        num = [num[0:length]]
        print("Length: %s, i: %s, num: %s" % (length, i, num))
        if i in num:
            print("/Pass %s" % i)
            continue
        num.append(i)
        if length < maximum:
            print("Depth + 1")
            length += 1
            rec(nums, num, maximum, length)
            print("Continuing + 1")
        else:
            print("!!!Depth - 1")
            nums.append(num)
            del num[-1]
            print(",,,Deleted last, num = %s" % num)
            length -= 1
            rec(nums, num, maximum, length)
            print("Continuing - 1")
        # WTF
    return nums


# print(rec([], [], 2, 0))
# print(nums)

# I tried many recursions after for loops, then returned to a for loop and completed it in a nasty fashion in 5 mins

# Answer: 2783915460
