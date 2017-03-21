from Scripts import is_prime
from math import sqrt


def get_corners(length):
    squares = []
    for i in range(3, length + 1, 2):
        squares.append(i ** 2)
    corners = []
    for square in squares:
        corners.append(square)
        base = int(sqrt(square)) - 1
        num = square
        for i in range(0, 3):
            num -= base
            corners.append(num)
    return corners


def get_percentage_prime(arr):
    total = 0
    for num in arr:
        if is_prime(num):
            total += 1
    return total / (len(arr) + 1) * 100


l = 5
corners = get_corners(l)

while get_percentage_prime(corners) > 10:
    if l % 5 == 0:
        print("At l = %s" % l)
    l += 200
    corners = get_corners(l)

l -= 200

for i in range(l - 200, l):
    print("At l = %s" % i)
    corners = get_corners(i)
    percent = get_percentage_prime(corners)
    if percent < 10:
        print("Answer: l = %s" % i)
        break
# Answer: 26241
