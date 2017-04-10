import math

for i in range(2, 100): # sqrt 1 and 100 rational
    square = (math.sqrt(i))
    if int(square) % 1 == 0:
        continue
    print(str(square))