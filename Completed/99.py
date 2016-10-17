with open("../Sources/99 Base Exp.txt", "r") as f:
    data = f.read()
    arr = data.split("\n")

print(arr)
count = 0
maximum = 0
maxcount = 0
a = [0]
length = len(arr)
for line in arr:
    count += 1
    print("At %s of %s" % (count, length))
    pair = line.split(",")
    b = int(pair[0])
    e = int(pair[1])
    r = b ** e
    a.append(r)
    if r > maximum:
        maximum = r
        maxcount = count

# print(maximum)
print(maxcount)

# Answer: 709
