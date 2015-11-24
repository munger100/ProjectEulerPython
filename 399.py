import sys
import math

number = 0
number_one = 0
number_two = 1
counter = 0


def count_divisors(num, opt="c" or "f"):  # don't use find, only count
    number_of_divisors = 0
    sr = math.sqrt(num)
    divisors = []

    for i in range(1, int(sr)):
        if num % i == 0:
            number_of_divisors += 2
            divisors.append(i)

    if sr * sr == num:
        number_of_divisors -= 1

    if opt == "c":
        return number_of_divisors

    if opt == "f":
        return divisors


def is_square_free(num):
    print("hey")


while True:
    number = number_one + number_two
    number_two = number_one
    number_one = number
    if number % 4 is not 0:
        counter += 1
        if counter == 200:
            print(number)
            print(count_divisors(10, "f"))
            sys.exit(number)