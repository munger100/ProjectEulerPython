import sys

maximum = 1000000000
counter = 0


def isPrime(num):
    global counter
    if num == 2:
        counter += 1
        return True
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    counter += 1
    return True


for number in range(2, 1000000000):
    if isPrime(number):
        if counter % 100 == 0:
            print(counter)
    if counter == 10001:
        print("10 001th prime found! ---> %s" % number)
        sys.exit(number)

print("Incomplete. Primes Found: %s" % counter)