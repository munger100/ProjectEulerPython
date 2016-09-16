count = 0


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_lychrel(n, limit=50):
    iteration = 0
    num = n
    while iteration < limit:
        num += int(str(num)[::-1])
        if is_palindrome(num):
            return False
        iteration += 1
    return True


for i in range(1, 10000):
    if i % 1000 == 0:
        print("At " + str(i))
    if is_lychrel(i):
        count += 1

print("Lychrel numbers: " + str(count))
# Answer: 249
