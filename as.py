sum = 0


def factorial(n):
    final = n
    r = n - 1
    while r is not 0:
        final *= r
        r -= 1
    return final

nums = []
total = 0
for num in str(145):
    nums.append(int(num))
for num in nums:
    total += factorial(num)
if total == int(145):
    sum += int(145)

print(sum)

print(factorial(1) + factorial(4) + factorial(5))
print(nums)
print(total)