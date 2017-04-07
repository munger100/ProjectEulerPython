def is_bouncy(n):
    return not is_ascending(n) and not is_descending(n)


def is_ascending(n):
    num = str(n)
    last = 0
    for digit in num:
        if int(digit) < last:
            return False
        last = int(digit)
    return True


def is_descending(n):
    num = str(n)
    last = 9
    for digit in num:
        if int(digit) > last:
            return False
        last = int(digit)
    return True

percentage = 0
bouncy = []
num = 99
while percentage < 99:
    num += 1
    if int(percentage) % 40 == 0:
        print("At num = %s, percentage = %s" % (num, percentage))
    if is_bouncy(num):
        # print("Bouncy!, ", num)
        bouncy.append(num)
    percentage = len(bouncy) / num * 100

print("Num = %s, Percentage = %s" % (num, percentage))
# print(is_ascending(538), is_descending(538), is_bouncy(538))