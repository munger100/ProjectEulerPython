__author__ = 'Matthew'

with open("grid 20x20", "r") as file:
    data = file.read()
    file.close()
lines = []
grid = [[]] * 20
counter = 0
line_count = 0
number_count = 0
greatest_product = 0

for a in data.split("\n"):
    counter += 1
    lines.append(a)
    for b in lines:
        nums = b.split(" ")
        for num in nums:
            grid[counter - 1] = nums


def get_number(line_num, number_num):
    return int(grid[line_num - 1][number_num - 1])


def check_greatest(greatest, product):
    if product > greatest:
        return product
    else:
        return greatest

for line in grid:
    line_count += 1
    for number in line:
        number_count += 1

        if len(line) - number_count >= 4:  # From left to right
            product = 1
            for i in range(4):
                product *= get_number(line_count, number_count + i)
            greatest_product = check_greatest(greatest_product, product)

        if len(grid) - line_count >= 4:  # From top to bottom
            product = 1
            for i in range(4):
                product *= get_number(line_count + i, number_count)
            greatest_product = check_greatest(greatest_product, product)

        if len(grid) - line_count >= 4 and len(line) - number_count >= 4:  # Diagonal Left to right, top to bottom
            product = 1
            for i in range(4):
                product *= get_number(line_count + i, number_count + i)
            greatest_product = check_greatest(greatest_product, product)

        if len(grid) - line_count >= 4 and len(line) - number_count >= 16:  # Diagonal Left to right, top to bottom
            product = 1
            for i in range(4):
                product *= get_number(line_count - i, number_count + i)
            greatest_product = check_greatest(greatest_product, product)

    number_count = 0


print("Greatest Product: %s" % greatest_product)
# Answer: 70600674
