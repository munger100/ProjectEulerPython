__author__ = 'Matthew'

import sys

pandigitals = list("123456789")
number = 0
number_one = 0
number_two = 1
counter = 0

while True:
    counter += 1
    number = number_one + number_two
    number_two = number_one
    number_one = number
    if sorted(list(str(number)[-9:])) == sorted(pandigitals) and sorted(list(str(number)[:9])) == sorted(pandigitals):
        print("F%s = %s" % (counter, number))
        sys.exit()
