largest = 0

for one in range(100, 1000):
    for two in range(100, 1000):
        num = one * two
        if str(num) == str(num)[::-1]:
            if num > largest:
                largest = num

print("Largest Palindrome Product of two 3 digit numbers is %s." % largest)
# Answer: 906609