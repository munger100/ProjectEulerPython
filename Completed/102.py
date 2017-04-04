# from sympy import *

with open("../Sources/102 Triangle containment.txt", "r") as f:
    data = f.read()


def get_quadrant(p):
    if p[0] * p[1] == 0:  # Point on line
        return 0
    if p[0] * p[1] > 0:  # 1 or 3
        return 1 if p[0] > 0 else 3
    return 4 if p[0] > 0 else 2


def find_slope(a, b):
    return ((b[1]) - (a[1])) / ((b[0]) - (a[0]))  # y2 - y1 / x2 - x1


def check_for_origin(points):
    valid = True
    a, b, c = points[0], points[1], points[2]

    # Make line with ab
    slope = find_slope(a, b)
    x = a[0]
    y = a[1]
    init = y - slope * x
    if (c[1] > slope * c[0] + init) != (0 > init):
        valid = False

    # Make line with bc
    if valid:
        slope = find_slope(b, c)
        x = b[0]
        y = b[1]
        init = y - slope * x
        if (a[1] > slope * a[0] + init) != (0 > init):
            valid = False

    # Make line with ac
    if valid:
        slope = find_slope(a, c)
        x = a[0]
        y = a[1]
        init = y - slope * x
        if (b[1] > slope * b[0] + init) != (0 > init):
            valid = False
    return valid


total = 0
number = 0
for triangle in data.split("\n"):
    number += 1
    arr = triangle.split(",")
    a = [int(arr[0]), int(arr[1])]
    b = [int(arr[2]), int(arr[3])]
    c = [int(arr[4]), int(arr[5])]
    points = [a, b, c]
    quadrants = []
    for point in points:
        quadrants.append(get_quadrant(point))
    if quadrants.count(quadrants[0]) == 3:
        continue  # Not in center
    counts = [0, 0, 0, 0, 0]
    for quadrant in quadrants:
        counts[quadrant] += 1
    if counts[0] == 0:
        if counts[1] == 2 and counts[3] == 1:
            total += 1 if check_for_origin(points) else 0
        elif counts[2] == 2 and counts[4] == 1:
            total += 1 if check_for_origin(points) else 0
        elif counts[3] == 2 and counts[1] == 1:
            total += 1 if check_for_origin(points) else 0
        elif counts[4] == 2 and counts[2] == 1:
            total += 1 if check_for_origin(points) else 0
        elif max(counts) == 1:
            total += 1 if check_for_origin(points) else 0
    else:
        total += 1 if check_for_origin(points) else 0

print("Total = %s" % total)
# Answer: 228
