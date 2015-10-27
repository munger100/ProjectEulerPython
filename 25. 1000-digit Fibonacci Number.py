import sys

number = 0
number_one = 0
number_two = 1
counter = 0

while True:
    number = number_one + number_two
    number_two = number_one
    number_one = number
    counter += 1
    if len(str(number)) == 1000:
        print(number)
        print(counter)
        sys.exit(number)