prime_big_number = 0
big_number = 600851475143
number = 2

while number * number < big_number:
    while big_number % number == 0:
        big_number /= number
    number += 1

print(int(big_number))
# Answer: 6857