nums = list(range(1, 101))

total = [0, 0]

for x in nums:
    total[0] += x
total[0] **= 2
for y in nums:
    total[1] += y ** 2

final = total[0] - total[1]

print(final)
# Answer: 25164150
