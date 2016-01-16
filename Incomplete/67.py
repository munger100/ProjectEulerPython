with open("../Sources/67 Max Path Sum II 2", "r") as f:
    data = f.read()


def sort_into_pyramid(data):
    array = []
    lines = data.split('\n')
    count = 0
    for line in lines:
        count += 1
        print(count)
        if count != 101:
            nums = line.split(' ')
            array.append([int(num) for num in nums])
    return array


def reverse(array):
    newarray = []
    for i in range(1, len(array) + 1):
        newarray.append(array[-i])
    return newarray


def greatest(a, b):
    return a if a >= b else b


pyramid = reverse(sort_into_pyramid(data))

for i in range(1, len(pyramid)):
    for j in pyramid[i]:
        index = pyramid[i].index(j)
        pyramid[i][index] += greatest(pyramid[i - 1][index], pyramid[i - 1][index + 1])

print(pyramid[-1])
