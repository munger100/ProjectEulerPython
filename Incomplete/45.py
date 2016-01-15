def get(num, mode):
    for arg in mode:
        arg(num)


def triangle(num):
    tri = num * (num + 1) / 2
    yield tri


def pentagon(num):
    penta = num * ((3 * num) - 1) / 2
    yield penta


def hexagon(num):
    hexa = num * ((2 * num) - 2)
    yield hexa


print(triangle(6))
# Answer: