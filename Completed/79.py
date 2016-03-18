import time

with open("../Sources/79 Passcode derivation.txt", "r") as f:
    data = f.read().strip()


def remove_duplicates(str):
    a = str.split("\n")
    n = []
    for i in a:
        if i not in n:
            n.append(i)
    return n


def get_smallest_combo(arr):
    n = []
    for i in arr:
        l = list(str(i))
        for char in l:
            if char not in n:
                n.append(char)
    return sorted(n)


def is_valid(num, lsc):
    for entry in entries:
        i = 0
        for char in lsc:
            if entry[i] == char:
                i += 1
            else:
                continue
            if i >= 3:
                break
        if i != 3:
            break
    if i == 3:
        print(counter)
        return num


def print_if(num, trig):
    if num % trig == 0:
        print(num)


def long_enough(num, smallest):
    return len(num) >= len(smallest)

start_time = time.time()
entries = remove_duplicates(data)
smallest_combo = get_smallest_combo(entries)
# print(smallest_combo)
# print(entries)

# Brute Force Attempt
solved = False
counter = 1

while not solved:
    print_if(counter, 1000000)
    lsc = list(str(counter))
    if not long_enough(lsc, smallest_combo):
        counter *= 10
        continue
    if is_valid(counter, lsc):
        break
    else:
        counter += 1

print("Answer is %i, Took about %i seconds" % (counter, time.time() - start_time))
# Answer: 73162890, Time on MSI: 144 seconds, Time on ASUS: