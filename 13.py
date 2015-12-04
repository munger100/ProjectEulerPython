total = 0
with open("number.txt", "r") as f:
    data = f.read()

number = data.split("\n")

for i in number:
    total += int(i)

print(str(total)[:10])
# Answer: 5537376230