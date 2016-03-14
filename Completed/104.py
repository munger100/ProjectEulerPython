__author__ = 'Matthew'

import time

pandigitals = sorted(list("123456789"))
number = 0
number_one = 0
number_two = 1
counter = 0
completed = False
start_time = time.time()
old_time = start_time
new_time = 0

while not completed:
    counter += 1
    number = number_one + number_two
    number_two = number_one
    number_one = number
    if counter % 10000 == 0:
        new_time = time.time()
        print(
            "At {number}th number ({percent}%), number length is {digits} digits, time since start: {tsincestart} minutes, time since last update: {tsincelastupdate} seconds".format(
                number=counter, percent=int(counter * 100 / 300000), digits=len(str(number)),
                tsincestart=str(int(new_time - start_time) / 60 + (int(new_time - start_time) % 60) / 60),
                tsincelastupdate=int(new_time - old_time)))
        old_time = new_time
    if sorted(list(str(number)[:9])) == pandigitals:
        if sorted(list(str(number)[-9:])) == pandigitals:
            print("F%s = %s" % (counter, number))
            completed = True
# Answer: 329468
