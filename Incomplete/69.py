maximum = 0
val = 0


def phy(num):
    count = 0
    for i in range(1, num):
        if num % i != 0:
            count += 1
    return count


def n_of_phy(num):
    p = phy(num)
    return num / p if p != 0 else 0

    # for i in range(1, 1000000 + 1):
    #     if i % 10000 == 0:
    #         print(i)
    #     n = n_of_phy(i)
    # if n > maximum:
    #     maximum = n
    #     val = i


print(phy(10))
# print(n_of_phy(10))
