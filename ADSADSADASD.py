file = open("numbers in letters.txt", "r")
vamped_file = "".join(file.read().split())
revamped_file = vamped_file.replace("-", "")
d = 0

for i in list(revamped_file):
    if i != " " or i != "-":
        d += 1

print(d)
print(revamped_file)