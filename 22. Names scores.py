import string

with open('names.txt', 'r') as f:
    data = f.read()

chars = list(string.ascii_uppercase)
chars.insert(0, "")
names = sorted(data.split("\",\""))
names.insert(0, "")
total = 0


def find_name_index(name):
    return names.index(name)


def find_alpha_index(char):
    return chars.index(char)


def find_name_score(name):
    score = 0
    for char in name:
        score += find_alpha_index(char)
    score *= find_name_index(name)
    return score


for name in names:
    total += find_name_score(name)

print(total)