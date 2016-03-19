from Sources import scripts

sum = 0

for number in range(3, scripts.factorial(9) * 9):  # Max = 3 265 920
    nums = []
    total = 0
    for num in str(number):
        nums.append(int(num))
    for num in nums:
        total += scripts.factorial(num)
    if total == int(number):
        sum += int(number)
    if number % 100000 == 0:
        print("At: " + str(number))

print(sum)
# Answer: 145