from Scripts import factorial


def add(num):
    sum = 0
    num = factorial(num)
    string = list(str(num))
    for i in string:
        sum += int(i)
    return sum


def start(num):
    print(add(num))


start(100)
# Answer: 648
