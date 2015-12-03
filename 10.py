import time
from scripts import *

file = open("primes.txt", "r+")
total = 2  # Starting with 2 because the code is made to skip all Even numbers, and 2 is the only even prime.
t = [None, None]
primes = {2, 3}
highest_prime = 0



t[0] = time.time()

for number in range(2, 2000000):
    if number == 2 or number % 2 != 0:
        if isPrime(number):
            total += number
        if number % 10001 == 0:
            t[1] = time.time()
            print("At %sth number. Time: %s" % (number, t[1] - t[0]))

print("Sum of all primes under 2'000'000: ---> " + str(total))
# Answer: 142913828922