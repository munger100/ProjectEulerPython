milestones = [1, 10, 100, 1000, 10000, 100000, 1000000]
num = []
count = 1
total = 1
while len(num) < 1000000:
    for i in str(count):
        num.append(int(i))
    count += 1

for m in milestones:
    total *= num[m - 1]

print(total)
# Answer: 210
