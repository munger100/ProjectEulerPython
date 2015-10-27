import math


class PrimeManager():
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11]
        self.prime_set = set(self.primes)

    def add_prime(self, number):
        self.primes.append(number)
        self.prime_set.add(number)

    def load(self):
        with open("primes.txt", "r") as f:
            data = f.read()
        data = data.split('\n')
        data = [int(i) for i in data if i.strip()]
        self.primes = data
        self.prime_set = set(self.primes)

    def cache(self):
        data = [str(i) for i in self.primes]
        open("primes.txt", "w").write('\n'.join(data))

    def is_prime(self, number):
        if number in self.prime_set:
            return True

        for prime in self.primes:
            if number % prime == 0:
                return False

        highest = self.primes[-1]
        for i in range(highest, number + 1):
            is_prime = True
            for prime in self.primes:
                if i % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                self.add_prime(i)

        if number in self.prime_set:
            return number in self.prime_set


def run_tests():
    pm = PrimeManager()
    pm.load()
    counter = 0
    for i in range(2000000):
        counter += 1

    if counter % 1000 == 0:
        print()

    print(", ".join([str(i) for i in pm.primes]))
    pm.cache()

if __name__ == "__main__":
    run_tests()

