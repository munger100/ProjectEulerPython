import sys

def isDivisible(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True

for num in range(2, 999999999, 2):
    if num % 2 == 0:  # Gotta be a multiple of 2.
        if isDivisible(num):
            print(num)
            sys.exit()