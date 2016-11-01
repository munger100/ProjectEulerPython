def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
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
        for i in range(1, int(num / 2) + 1):
            if num % i == 0:
                d.append(i)
        d.append(num)
    return d
