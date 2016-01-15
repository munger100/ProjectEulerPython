import string

counter = 0

with open('../Sources/42 Coded triangle numbers words.txt', 'r') as f:
    data = f.read()
    words = data.split("\",\"")

with open('../Sources/42 Coded Triangle Numbers values.txt', 'r') as r:
    values = r.read().split("\n")

chars = list(string.ascii_uppercase)
reversed_list = list(reversed(chars))
reversed_list.append("Placeholder")
chars = list(reversed(reversed_list))


def triangle(num):
    t = (num / 2) * (num + 1)
    return int(t)


for word in words:
    count = 0
    for char in word:
        count += chars.index(char)
    if values.count(str(count)) == 1:
        counter += 1

print(counter)
# Answer: 162
