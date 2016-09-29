import sys

from Sources import scripts

maximum = 1000000000
counter = 0

for number in range(2, 1000000000):
    if number is 2 or number % 2 != 0:
        if scripts.isPrime(number):
            counter += 1
            if counter % 1000 == 0:
                print("Primes Found: " + str(counter))
        if counter == 10001:
            print("10 001th prime found! ---> %s" % number)
            sys.exit(number)

print("Incomplete. Primes Found: %s" % counter)
# Answer: 104743
