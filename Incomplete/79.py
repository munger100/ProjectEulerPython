with open("../Sources/79 Passcode derivation.txt", "r") as f:
    data = f.read()

print(data.strip())


def remove_duplicates(str):
    a = str.split("\n")
    n = []
    for i in a:
        if i not in n:
            n.append(i)


remove_duplicates(data)
