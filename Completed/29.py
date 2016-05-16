distinct_powers = []

for a in range(2, 101):
    print("At " + str(a))
    for b in range(2, 101):
        val = a ** b
        if val not in distinct_powers:
            distinct_powers.append(val)

print("Distinct powers: " + str(len(distinct_powers)))
# Answer: 9183