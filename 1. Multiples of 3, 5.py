total = 0

for number in range(1000):
    if number % 3 == 0:
        total += number
    if number % 5 == 0:
        if number % 3 != 0:  # So it doesn't print the same number twice
            total += number