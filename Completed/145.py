def is_reversible(n):
    s = n + int(''.join(reversed(str(n))))
    for digit in str(s):
        if int(digit) % 2 == 0:
            return False
    return True


reversibles = []
for i in range(1, 1000000000):
    if i % 1000000 == 0:
        print("At i = %s" % i)
    if i % 10 == 0:
        continue
    if is_reversible(i):
        reversibles.append(i)

print(len(reversibles))
# Answer: 608720
