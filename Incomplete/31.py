currencies_default = [1, 2, 5, 10, 20, 50, 100, 200]  # 1p, 2p, 5p, 10p, 20p, 50p, 1E, 2E
currencies_reverse = currencies_default.reverse()
two_euros = 200
pieces = currencies_default
combos = []


def add_piece(piece, total):
    total += piece


def check(total):
    if total == 200:
        return 1
    elif total > 200:
        return 2
    else:
        return 0


def recursion(depth):
    for piece in currencies_reverse:
        print(None)
        # Tried recursion, failed badly
