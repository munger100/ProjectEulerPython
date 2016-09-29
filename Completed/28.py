import math

largest_number = 1001 * 1001
init = 1001 + 2
total = 0


def generate():
    arr = []
    for i in range(1, init, 2):
        arr.append(i)
    return arr


depth = generate()

# print(depth)

for d in depth:
    # print("At %s of %s, only uneven numbers" % (d, depth[-1]))
    max_of_depth = d ** 2
    num = max_of_depth
    for i in range(0, 3 + 1):
        num = max_of_depth - (i * (d - 1))
        if num == 1:
            # print(num)
            total += num
            break
        elif num > 0:
            # print(num)
            total += num
        else:
            break

print("Largest: %s, Last: %s" % (largest_number, max_of_depth))
print("Sum of Diagonals: %s " % total)
#  Answer: 669171001
