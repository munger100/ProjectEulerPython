def is_divisible(number, max):
    for i in range(1, max + 1):
        if number % i != 0:
            return False
    return True


num = 222792000
while not is_divisible(num, 20):
    num += 2

print(num)
# Answer: 232792560
