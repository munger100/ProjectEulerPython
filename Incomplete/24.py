numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 1000000000
th = 0


def is_lex(num):
    return sorted(list(str(num))) == numbers

print(numbers)

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
