def factorial(num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i
    return sum


def calculator(num):
    result = (factorial(2 * num)) / (factorial(num) ** 2)
    return int(result)


print(calculator(20))
# Answer: 137846528820
