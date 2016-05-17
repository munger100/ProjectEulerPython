product = 0
greatest_sequence = 0


def is_prime(n):
    for i in range(2, abs(n)):
        if n % i == 0:
            return False
    return True


def get_sequence(a, b):
    prime = True
    n = -1
    while prime:
        n += 1
        prime = is_prime(n ** 2 + a * n + b)
    return n


for a in range(-999, 1000):
    print("A: %i" % a)
    for b in range(-999, 1000):
        seq = get_sequence(a, b)
        if seq > greatest_sequence:
            greatest_sequence = seq
            product = a * b
            print("Greatest Sequence: %i, Product: %i" % (greatest_sequence, product))

print("[END] Greatest Sequence: %i, Product: %i" % (greatest_sequence, product))
# Answer: -59231