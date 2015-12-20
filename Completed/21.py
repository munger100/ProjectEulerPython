total = 0
nums = []


def d(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total


for a in range(1, 10000):
    if a % 1000 == 0:
        print("At %s" % a)

    b = d(a)
    if d(b) == a and a != b:
        nums.append(a) if nums.count(a) < 1 else None
        nums.append(b) if nums.count(b) < 1 else None

for num in nums:
    total += num

print(total)
# Answer: 31626
