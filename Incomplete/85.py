def grid(x, y):
    rectangle_count = 0
    for w in range(1, x + 1):
        for h in range(1, y + 1):
            tw = int(x / w)
            tw += x % w
            th = int(y / h)
            th += y % h
            this_count = tw * th
            rectangle_count += this_count
    return rectangle_count


greatest = 0
area = [None]
print(grid(3, 2))

for x in range(1, 25000):
    if x % 100 == 0:
        print("At x = %s" % x)
    for y in range(1, 25000):
        rect_count = grid(x, y)
        if rect_count > greatest:
            grid_area = x * y
            if rect_count < 2000000:
                greatest = rect_count
                area[0] = [rect_count, grid_area]
            else:
                area.append([rect_count, grid_area])
                break
new_greatest = 0
new_area = [0]
for rcs in area:
    if rcs[0] > new_greatest:
        new_greatest = rcs[0]
        new_area = [[new_greatest, rcs[1]]]

print(new_area)
