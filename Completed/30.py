limit = 355000
sum = 0

for num in range(2, limit):
    if num % 100000 == 0:
        print("Trying %s" % num)
    added = 0
    for integer in str(num):
        added += int(integer) ** 5
    if added == num:
        sum += num

print(sum)
# Answer: 443839
