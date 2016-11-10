import time

from Scripts import is_prime

total = 0
t = [None, None]

t[0] = time.time()

for number in range(2, 2000000):
    if number == 2 or number % 2 != 0:
        if is_prime(number):
            total += number
        if number % 10001 == 0:
            t[1] = time.time()
            print("At %sth number. Time taken: %s" % (number, t[1] - t[0]))

print("Sum of all primes under 2'000'000: ---> " + str(total))
# Answer: 142913828922
