total = 0
with open("../Sources/13 Large Sum.txt", "r") as f:
    data = f.read()

number = data.split("\n")

for i in number:
    total += int(i)

print(str(total)[:10])
# Answer: 5537376230