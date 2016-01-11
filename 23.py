max = 28123
total = 0
deficients = []
perfects = []
abundants = []


def is_abundant(n):
    l = []
    t = 0
    for num in range(1, n + 1):
        if n % num == 0 and num is not n:
            l.append(num)
    for num in l:
        t += num
    if t > n:
        abundants.append(n)
        return True
    else:
        return False


def can_be_sum(n):
    for a in abundants:
        for b in abundants:
            if a + b == i:
                return False
            else:
                continue
    return True


for i in range(1, max + 1):
    if can_be_sum(i):
        total += i
    print(i) if i % 1000 == 0 else None
    is_abundant(i)

print(total)
print(abundants)