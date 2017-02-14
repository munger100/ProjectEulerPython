currencies_default = [1, 2, 5, 10, 20, 50, 100, 200]  # 1p, 2p, 5p, 10p, 20p, 50p, 1E, 2E
currencies_reverse = reversed(currencies_default)
two_euros = 200
pieces = currencies_default
combos = []


def check(total):
    if total == 200:
        return 1
    elif total > 200:
        return 2
    else:
        return 0


for i in range(0, len(currencies_default)):
    total = 0
    count = 0
    while total < 200:
        count += 1
        total += currencies_default[i]
    print(currencies_default[i], total, count)

d = dict()
for a in currencies_default:
    for b in currencies_default:
        if int(a / b) > 0:
            d[str(a) + "," + str(b)] = int(a / b)
            # d.__setitem__(str(a) + "," + str(b), a / b)
t = 1
a = 0
for val in d.values():
    t *= int(val)
    a += int(val)
arr = [1]
for a in range(0, len(currencies_default)):
    for b in range(currencies_default[a], 201):
        arr[b] += arr[b - currencies_default[a]]

print(arr[-1])

print(t)
print(a)
print(d)


# def recursion(depth):
#     for piece in currencies_reverse:
#         print(None)
# Tried recursion, failed badly
