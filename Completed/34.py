from Scripts import factorial

sum = 0

for number in range(3, factorial(9) * 9):  # Max = 3 265 920
    nums = []
    total = 0
    for num in str(number):
        nums.append(int(num))
    for num in nums:
        total += factorial(num)
    if total == int(number):
        sum += int(number)
    if number % 100000 == 0:
        print("At: " + str(number))

print(sum)
# Answer: 145
