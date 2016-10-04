def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def fib(num):
    return (num - 1) + (num - 2)


def get_divisors(num):
    d = []
    if num < 100:
        for i in range(1, num + 1):
            if num % i == 0:
                d.append(i)
    else:
        for i in range(1, int(num/2) + 1):
            if num % i == 0:
                d.append(i)
        d.append(num)
    return d

