from math import cos, sin, tan, atan, pi, sqrt


def rad_to_deg(rad):
    return rad * 180 / pi


def get_percentage(n):
    # n = Circles
    blue = (1 - (pi * .5 ** 2)) / 4
    l = 1
    w = n
    #  Tan = opp / adj = w / l
    angle = atan(w / l)
    circle = 2 * pi
    angle = circle / 4 - angle
    angle = rad_to_deg(angle)
    tw = 0.5
    th = None
    return angle


def c(x):
    h = 0.5
    k = 0.5
    return sqrt(1 / ((x - h) ** 2)) + k


def y(x, n):
    y2 = 1
    y1 = 0
    x2 = n
    x1 = 0
    a = (y2 - y1) / (x2 - x1)
    b = 0
    return a * x + b


for i in range(0, 2, float(0, 2)):
    if y(i, 2) == c(i):
        print(i)

print(get_percentage(2))
