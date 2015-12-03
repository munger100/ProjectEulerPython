def pythagoreantriplet():
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
    return 0


abc = pythagoreantriplet()
product = abc[0] * abc[1] * abc[2]  # All in an array just for you Mr Spence :)

print("The product of the pythagorean triplet for which a + b + c = 1000 is: ---> %s" % product)
# Answer: 31875000