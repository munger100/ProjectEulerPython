# Needs optimization
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


non_bouncy = []
num = 99
while num < 10 ** 100:
    num += 1
    if len(non_bouncy) % 1000 == 0:
        print("At non_bouncy count = %s, num = %s" % (len(non_bouncy), num))
    if not is_bouncy(num):
        non_bouncy.append(num)

print("Length of non_bouncy = %s" % non_bouncy)

