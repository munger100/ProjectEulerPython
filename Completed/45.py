def triangle(num):
    tri = num * (num + 1) / 2
    return int(tri)


def pentagon(num):
    penta = (num * (3 * num - 1)) / 2
    return int(penta)


def hexagon(num):
    hexa = num * (2 * num - 1)
    return int(hexa)


count = 0
pents = []
hexs = []
i = 0

while count < 2:
    if i % 1000 == 0:
        print("At %s" % i)
    tri = triangle(i)
    if tri in pents and tri in hexs:
        count += 1
        print("Found %s in each" % tri)
    pents.append(pentagon(i))
    hexs.append(hexagon(i))
    i += 1

print("Answer: %s" % tri)

# Answer: 1533776805
