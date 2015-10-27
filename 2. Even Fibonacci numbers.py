import sys

number = 0
number_one = 0
number_two = 1
total = 0

while True:
    number = number_one + number_two
    number_two = number_one
    number_one = number
    if number % 2 == 0:
        if not number > 4000000:
            total += number
        else:
            print(total)
            break