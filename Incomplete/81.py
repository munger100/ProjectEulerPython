with open('../Sources/81 Matrix.txt', 'r') as f:
    data = f.read()


def sort_data(data):
    ls = data.split("\n")
    index = 0
    lines = []
    for l in ls:
        lines.append(None)
        arr = []
        for a in l.split(","):
            arr.append(int(a))
        lines[index] = arr
        index += 1
    return lines


def get_entry(loc):
    if loc == [None, None]:
        return None
    return lines[loc[0]][loc[1]]


lines = sort_data(data)
total = 0

# Top-right

# count = [0, 0]
# for line in lines:
#     current = count
#     first = [current[0], current[1] + 1]
#     second = [current[0] + 1, current[1]]
#     opt = [first, second]
#     res = [get_entry(first), get_entry(second)]
#     highest = min(res)
#     count = opt[res.index(highest)]
#     total += highest

# Bottom-left

count = [79, 79]
while count[0] > 0 and count[1] > 0:
    print(count)
    current = count
    if current[1] - 1 < 0:
        second = [current[0] - 1, current[1]]
        first = [None, None]
    elif current[0] - 1 < 0:
        first = [current[0], current[1] - 1]
        second = [None, None]
    else:
        first = [current[0], current[1] - 1]
        second = [current[0] - 1, current[1]]
    opt = [first, second]
    res = [get_entry(first), get_entry(second)]
    if None in res:
        res.remove(None)
    print(res)
    highest = min(res)
    count = opt[res.index(highest)]
    total += highest

print(total)

pass  # Dbg
