from math import cos, sin, tan, atan, acos, asin, pi, sqrt
from sympy import *


def rad_to_deg(rad):
    return rad * 180 / pi


def get_percentage(n):
    # n = Circles
    r = 0.5
    blue = float((1 - (pi * r ** 2)) / 4)
    # Area triangle
    p = find_meeting_point(n)
    x, y = p[0], p[1]
    h = y
    b = r
    big_orange = b * h / 2
    # find angle of segment
    a = r
    b = r
    c = sqrt((0.5 - x) ** 2 + (0 - y) ** 2)
    theta = acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    segment_area = area_of_segment(n, theta, c)
    # big_orange = 0.5 * y / 2
    orange = big_orange - segment_area
    percent = float(orange) / float(blue) * 100
    return float(percent)


def c(x):
    h = 0.5
    k = 0.5
    r = 0.5
    return sqrt(1 / ((x - h) ** 2)) + k


def find_meeting_point(n):
    x = symbols('x')
    x = min(list(solveset(Eq(x ** 2 - x + x ** 2 / n ** 2 - x / n, -0.25), x)))
    y = 1 / n * x
    return x, y


def area_triangle_hero_formula(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def area_of_segment(n, theta, c):
    r = 0.5
    # area of sector - triangle
    sector = area_of_sector(r, theta)
    triangle = area_triangle_hero_formula(r, r, c)
    return sector - triangle


def area_of_sector(r, theta):
    a = r ** 2 * theta / 2
    return a


for i in range(0, 5000):
    if i % 10 == 0:
        print("i = %s" % i)
    percent = get_percentage(i)
    print("percent(%s) = %s" % (i, percent))
    if 0 < percent < (0.1):
        print(i, percent)
        break

# Answer: 2240
