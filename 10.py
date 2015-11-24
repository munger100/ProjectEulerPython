import time
import scripts

file = open("primes.txt", "r+")
total = 2  # Starting with 2 because the code is made to skip all Even numbers, and 2 is the only even prime.
t = [None, None]
primes = {2, 3}


class PrimeThing:
    def __init__(self, data):
        self.primes = data.read().split("\n")
        self.highest_prime = 0
        print(self.primes)

    def isPrime(self, num):
        scripts.is_prime(num)


p = PrimeThing(file)
t[0] = time.time()

for number in range(1, 2000000, 2):
    if number != 1:
        if p.isPrime(number):
            total += number
        if number % 10000 == 0:
            t[1] = time.time()
            print("At %sth number. Time: %s" % (number, t[1] - t[0]))
            t[0] = t[1]

print("Sum of all primes under 2'000'000: ---> " + str(total))