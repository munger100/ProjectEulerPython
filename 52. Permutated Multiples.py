___author___ = "Matthew"
import sys


def math(x, y, c):
    return c == sorted(list(str(x * y)))


for x in range(1, 1000000000):
    comparison = sorted(list(str(x)))
    if math(x, 2, comparison):
        if math(x, 3, comparison):
            if math(x, 4, comparison):
                if math(x, 5, comparison):
                    if math(x, 6, comparison):
                        print(comparison)
                        sys.exit("Found it: %s" % x)

                        # Answer = 142857
