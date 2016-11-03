# num = 10000
# total = 300000
# print(num * 100 / total)

# num = [1, 5, 6, 3, 6, 8]
# print("Count 1 000 000: Number = %s" % (''.join(map(str, num))))

# print(1/7)

# arr = [1, 5, 10, 15, 20]
#
# for a in arr:
#     print(arr)
    # print(arr)
    # arr[arr.index(a)] = a + 1
    # print(a)
    # arr[-1] = 0
#
# print(arr)

# a = "asdasds"
# b = list(a)
# print(a)
# print(b)
# print(''.join(b))


def is_pandigital(n):
    n = str(n)
    for i in range(1, len(n) + 1):
        if str(i) not in n:
            return False
    return True

print(is_pandigital(999999999))