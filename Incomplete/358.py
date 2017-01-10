max_length = 6
answer = 142857
# answer = 0588235294117647
left = "00000000137"
right = "56789"

from Scripts import is_prime


def is_cyclic(n):  # n must be str
    n = str(n)
    m = len(n)
    init = n = list(n)
    while n[0] == "0":
        del n[0]
    n = int(''.join(n))
    # print("init(n) == %s" % init)
    cyc = True
    for i in range(2, m):
        x = n * i
        init_temp = list(str(x))
        # print("init_temp) == %s" % init_temp)
        y = init_temp
        y.append(y.pop(0))
        a = False
        for i in range(1, len(y)):
            if y == init:
                a = True
                # print(y)
                break
            y.append(y.pop(0))
        if not a:
            cyc = False
            # print(y)
    return cyc


ints = [i for i in range(0, 10)]

# for i in range(9, -1, -1):
#     print(i)
start = 0
limit = 100000000000000000000
for i in range(start, limit):
    if i % 100000 == 0:
        print("i = %s" % i)
    n = left + str(i) + right
    if is_cyclic(n):
        print("i = %s, n  = %s" % (i, n))
        t = 0
        for j in n:
            t += j
        print("t = %s" % t)
        break


# print(ints)

# for i in range(10, max_length):
#     is_cyclic(i)
# print(is_cyclic(100))
# print(is_cyclic(answer))
