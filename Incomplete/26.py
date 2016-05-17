def is_repetitive(num):
    val = 1 / 7
    end = list(str(val))[2:]
    for i in range(1, 10):
        first = []
        match = []
        for j in range(0, i):
            first.append(end[j])
        for k in range(i, i + i):
            match.append(end[k])
        if first == match:
            y = None
            for x in range(0, len(first)):
                if first[x] == y:
                    print(first, match)
                    return False
                y = first[x]
            return len(first)
    return False
print(1/7, 1/9)
# greatest = 0
# val = 0
# for d in range(2, 1001):
#     dec = is_repetitive(1 / d)
#     if dec is not False:
#         if dec > greatest:
#             greatest = dec
#             val = d
# print("Val: " + str(val) + ", Greatest: " + str(greatest))
