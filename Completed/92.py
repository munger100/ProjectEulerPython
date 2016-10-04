counter = 0
maximum = 10000000

for i in range(1, maximum):
    if i % 50000 == 0:
        print("At {0}".format(i))
    x = i
    while x != 1 and x != 89:
        s = str(x)
        a = list(s)
        x = 0
        for c in a:
            x += int(c) ** 2
    if x == 89:
        counter += 1

print("Amount of starting numbers which will hit 89: {0}".format(counter))
# haha took me 4 minutes to code
# Answer: 8581146
