def factorial(n):
    final = n
    r = n - 1
    while r > 0:
        final *= r
        r -= 1
    return final


def isPrime(num):
    if num == 2:
        return True
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True
