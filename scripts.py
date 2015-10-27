def factorial(n):
    final = n
    r = n - 1
    while r > 0:
        final *= r
        r -= 1
    return final