def factorial(num):
    if num == 1:
        return True
    else:
        return num * factorial(num - 1)


def isPrime(num):
    if num == 2:
        return True
    if num % 2 != 0:
        for i in range(2, num - 1):
            if num % i == 0:
                return False
    return True