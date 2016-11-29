with open("../Sources/89 Roman Numerals.txt", "r") as f:
    data = f.read()
nums = data.split("\n")

l = ["M", "D", "C", "L", "X", "V", "I"]

for num in nums:
    init_length = len(num)
    minimal = True
    vals = {}
    for letter in num:
        if letter in vals.keys():
            vals[letter] += 1
        else:
            vals[letter] = 1

    print(num, vals)
    break

"""
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    Numerals must be arranged in descending order of size.
    M, C, and X cannot be equalled or exceeded by smaller denominations.
    D, L, and V can each only appear once.

    Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
    I can only be placed before V and X.
    X can only be placed before L and C.
    C can only be placed before D and M.
"""
