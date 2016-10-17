with open("../Sources/67 Max Path Sum II 2", "r") as f:
    data = f.read()


def sort_into_pyramid(data):
    array = []
    lines = data.split('\n')
    count = 0
    for l in lines:
        count += 1
        # print(count)
        if count != 101:
            nums = l.split(' ')
            array.append([int(num) for num in nums])
    # print(data, array)
    return array


def reverse(array):
    new_array = []
    for i in range(1, len(array) + 1):
        new_array.append(array[-i])
    # print(array, new_array)
    return new_array


def greatest(a, b):
    return a if a >= b else b


pyramid = reverse(sort_into_pyramid(data))

index = [0, 0]
index[0] = 0
for line in pyramid:
    index[1] = 0
    for num in line:
        print(index)
        if index[1] == len(line) - 1:
            continue
        pyramid[index[0] + 1][index[1]] += greatest(pyramid[index[0]][index[1]], pyramid[index[0]][index[1] + 1])
        index[1] += 1
    index[0] += 1

print(pyramid[-1])

# Answer: 7273
