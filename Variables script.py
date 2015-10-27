__author__ = 'iCan Student'

class Variables():
    def __init__(self):
        self.hD = 0
        self.dict = {}


v = Variables()  # Setting Highest Divisor. Currently 0


def add_to_dict(num, divisors):
    v.dict[num] = divisors


def prepare_dict():
    for num in range(1, 51):
        number_of_divisors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                number_of_divisors += 1
        add_to_dict(num, number_of_divisors)
    print("Done Initiation")