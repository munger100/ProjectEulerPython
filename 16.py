import math

number = int(math.pow(2, 1000))
total = 0

for i in list(str(number)):
    total += int(i)

print(total)