import time
import math

total = 0
natural_number = 1
highestDivisor = 0
start_time = time.time()
goal = 500


def count_divisors(number):
    number_of_divisors = 0
    sr = math.sqrt(number)

    for i in range(1, int(sr)):
        if number % i == 0:
            number_of_divisors += 2

    if sr * sr == number:
        number_of_divisors -= 1

    return number_of_divisors


while count_divisors(total) < 500:
    total += natural_number
    natural_number += 1

print(total)
print("Time Taken: " + str(time.time() - start_time) + " seconds")
# Answer: 76576500