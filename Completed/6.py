num = list(range(1, 101))
total = [0, 0]

for x in num:
    total[0] += x
total[0] **= 2
for y in num:
    total[1] += y ** 2

final = total[0] - total[1]

print(final)
# Answer: 25164150
