largest = [0, 0, 0, 0]
total = 0

for a in range(1, 100):
    print("At A = %s" % a)
    for b in range(1, 100):
        count = 1
        total = 0
        for c in range(1, b):
            count *= a
        for char in str(count):
            total += int(char)
        if total > largest[3]:
            largest = count, a, b, total

print("Largest number: A = %s, B = %s, Number = %s" % (largest[1], largest[2], largest[0]))
print("Answer: %s" % largest[3])
# Answer: 972