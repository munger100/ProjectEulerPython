__author__ = 'Matthew'
import sys
from itertools import islice
from collections import Counter


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


with open("poker.txt") as f:
    rawdata = f.read()

hands = rawdata.split("\n")
player1wins = 0
player2wins = 0
draws = 0
ranks = ["two", "thr", "fou", "fiv", "six", "sev", "eig", "nin", "t", "j", "q", "k", "a"]


def play(h1, h2):
    winner = None
    player1wins = 0
    player2wins = 0
    draws = 0
    s1 = evaluate(h1)
    s2 = evaluate(h2)
    winner = define_winner(s1, s2)
    if winner == 1:
        player1wins += 1
    if winner == 2:
        player2wins += 1
    if winner == 0:
        draws += 1
    return player1wins, player2wins, draws


def define_winner(s1, s2):
    if s1[0] > s2[0]:
        winner = 1
        return winner
    elif s1[0] < s2[0]:
        winner = 2
        return winner
    elif s1[0] == s2[0]:
        if isinstance(s1[1], int) or isinstance(s2[1], int):  # This should never happen
            if s1[1] > s2[1]:
                winner = 1
                return winner
            if s1[1] < s2[1]:
                winner = 2
                return winner
            elif s1[1] == s2[1]:
                sys.exit("WTF SOMETHING IS WRONG %s & %s" % (s1, s2))
        else:  # I think this is where its wrong... probably in give_second_part()
            for i in range(0, 5):
                ar1 = []
                for thing in s1[1]:
                    ar1.append(get_rank(thing))
                ar2 = []
                for thing in s2[1]:
                    ar2.append(get_rank(thing))
                thing1 = sort_backwards(ar1)
                thing2 = sort_backwards(ar2)
                if thing1[i] > thing2[i]:
                    winner = 1
                    return winner
                elif thing1[i] < thing2[i]:
                    winner = 2
                    return winner
        sys.exit("SOMETHING BAD HAPPENED... s1: %s, s2 %s" % (s1, s2))


def evaluate(hand):
    """
        High Card: 1
        One Pair: 2
        Two Pairs: 3
        Three of a Kind: 4
        Straight: 5
        Flush: 6
        Full House: 7
        Four of a Kind: 8
        Straight Flush: 9
        Royal Flush: 10
    """
    flags = set_flags(hand)
    if is_flush(flags):  # Is either a Flush (6 pts), Straight Flush (9 pts) or Royal Flush (10 pts)
        flags = remove_suits(flags)
        if is_royal_straight(flags):  # Is a Royal Straight Flush (10)
            return 10, None
        elif is_straight(flags):  # Is a Straight Flush (9)
            return 9, give_highest_in_straight(flags)
        else:  # Is a Flush (6)
            return 6, give_second_part(flags, 6)
    else:  # Does not contain a Flush
        flags = remove_suits(flags)
        if is_four_of_a_kind(flags):  # Is a Four of a Kind (8)
            return 8, give_second_part(flags, 8)
        if has_triple(flags):  # Is either a Three of a Kind (4 pts) or a Full House (7 pts)
            if has_pair(flags):  # Is a Full House (7)
                return 7, give_second_part(flags, 7)

            else:  # Is a Three of a Kind (4)
                return 4, give_second_part(flags, 4)
        if has_pair(flags):  # Is either a Pair (2 pts) or a Double Pair (3 pts)
            if has_double_pair(flags):  # Has Two Pairs (3)
                return 3, give_second_part(flags, 3)
            else:  # Has a Pair (2)
                return 2, give_second_part(flags, 2)
        if is_straight(flags):  # Has a regular Straight
            return 5, give_highest_in_straight(flags)
        return 1, give_second_part(flags, 1)  # Highest wins


def give_sorted_backwards(array):
    if len(array) == 5:
        new_array = []
        cnt = Counter()
        for element in array:
            cnt[element] += 1
        keys = cnt.keys()
        values = cnt.values()
        for key, value in cnt:
            new_array.append()
    else:
        print("whoops")
        return 0


def give_second_part(flags, mode=1 or 2 or 3 or 4 or 6 or 7 or 8):
    container = []
    for card, count in flags.items():  # Put all cards in hand into a container
        if count >= 1:
            for i in range(count):
                container.append(card)
    ranks = container
    if mode == 1:
        ranks.sort(reverse=True)
        return ranks
    if mode == 2:
        var = Counter(ranks)
        ranks.sort(key=lambda x: (var[x], x), reverse=True)
        return ranks
    if mode == 3:
        var = Counter(ranks)
        ranks.sort(key=lambda x: (var[x], x), reverse=True)
        return ranks
    if mode == 4:
        var = Counter(ranks)
        ranks.sort(key=lambda x: (var[x], x), reverse=True)
        return ranks
    if mode == 6:
        var = Counter(ranks)
        ranks.sort(key=lambda x: (var[x], x), reverse=True)
        return ranks
    if mode == 7:
        var = Counter(ranks)
        ranks.sort(key=lambda x: (var[x], x), reverse=True)
        return ranks
    if mode == 8:
        var = Counter(ranks)
        ranks.sort(key=lambda x: (var[x], x), reverse=True)
        return ranks


def get_rank(c):
    if ranks.count(c) == 1:
        return int(ranks.index(c) + 2)
    else:
        print("ERROR: %s isn't a valid card!!!" % (c))
        return ValueError


def set_flags(hand):
    # Creates a dictionary with the frequencies of Faces and suits
    flags = {"two": 0, "thr": 0, "fou": 0, "fiv": 0, "six": 0, "sev": 0, "eig": 0, "nin": 0, "t": 0, "j": 0, "q": 0,
             "k": 0, "a": 0, "spades": 0, "clubs": 0, "hearts": 0, "diamonds": 0}
    for c in hand:
        if c[0] == "2":
            flags.__setitem__("two", flags.get("two") + 1)
        elif c[0] == "3":
            flags.__setitem__("thr", flags.get("thr") + 1)
        elif c[0] == "4":
            flags.__setitem__("fou", flags.get("fou") + 1)
        elif c[0] == "5":
            flags.__setitem__("fiv", flags.get("fiv") + 1)
        elif c[0] == "6":
            flags.__setitem__("six", flags.get("six") + 1)
        elif c[0] == "7":
            flags.__setitem__("sev", flags.get("sev") + 1)
        elif c[0] == "8":
            flags.__setitem__("eig", flags.get("eig") + 1)
        elif c[0] == "9":
            flags.__setitem__("nin", flags.get("nin") + 1)
        elif c[0] == "T":
            flags.__setitem__("t", flags.get("t") + 1)
        elif c[0] == "J":
            flags.__setitem__("j", flags.get("j") + 1)
        elif c[0] == "Q":
            flags.__setitem__("q", flags.get("q") + 1)
        elif c[0] == "K":
            flags.__setitem__("k", flags.get("k") + 1)
        elif c[0] == "A":
            flags.__setitem__("a", flags.get("a") + 1)
        if c[1] == "S":
            flags.__setitem__("spades", flags.get("spades") + 1)
        elif c[1] == "C":
            flags.__setitem__("clubs", flags.get("clubs") + 1)
        elif c[1] == "H":
            flags.__setitem__("hearts", flags.get("hearts") + 1)
        elif c[1] == "D":
            flags.__setitem__("diamonds", flags.get("diamonds") + 1)
    return flags


def remove_suits(flags):  # Clear a hand of its suits
    if "spades" in flags: del flags["spades"]  # Removing Suits, Avoiding KeyError
    if "clubs" in flags: del flags["clubs"]  # Removing Suits Avoiding KeyError
    if "diamonds" in flags: del flags["diamonds"]  # Removing Suits Avoiding KeyError
    if "hearts" in flags: del flags["hearts"]  # Removing Suits Avoiding KeyError
    return flags


def is_four_of_a_kind(flags):
    for card, count in flags.items():
        if count == 4:
            return True
    return False


def has_triple(flags):
    for card, count in flags.items():
        if count == 3:
            return True
    return False


def has_pair(flags):
    for card, count in flags.items():
        if count == 2:
            return True
    return False


def has_double_pair(flags):
    counter = 0
    for card, count in flags.items():
        if count == 2:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def is_flush(flags):
    if flags.get("spades") == 5 or flags.get("diamonds") == 5 or flags.get("hearts") == 5 or flags.get("clubs") == 5:
        return True
    else:
        return False


def is_royal_straight(flags):
    container = []
    for card, count in flags.items():  # Put all cards in hand into a container
        if count == 1:
            container.append(card)
    ranks = []
    for item in container:  # Get ranks of each card, to check for straight
        ranks.append(get_rank(item))
    ranks = sorted(ranks)  # Place ranks in increasing order
    if ranks[0] == 10:  # If lowest card in straight is 10, it is automatically a 10, J, Q, K, A AKA Royal Straight
        return True
    else:
        return False


def is_straight(flags):
    container = []
    for card, count in flags.items():  # Put all cards in hand into a container
        if count == 1:
            container.append(card)
    ranks = []
    for item in container:  # Get ranks of each card, to check for straight
        ranks.append(get_rank(item))
    ranks = sorted(ranks)  # Place ranks in increasing order
    prev = ranks[0]
    for rank in ranks[1:len(ranks)]:
        if rank == prev + 1:
            prev = rank
            continue
        else:
            return False
    return True


def give_highest_in_straight(flags):
    container = []
    for card, count in flags.items():  # Put all cards in hand into a container
        if count == 1:
            container.append(card)
    ranks = []
    for item in container:  # Get ranks of each card, to check for straight
        ranks.append(get_rank(item))
    ranks = sorted(ranks)  # Place ranks in increasing order
    prev = ranks[0]
    for rank in ranks[1:len(ranks)]:
        if rank == prev + 1:
            prev = rank
            continue
        else:
            return False
    return ranks[-1]


def give_highest(flags):
    container = []
    for card, count in flags.items():  # Put all cards in hand into a container
        if count > 0:
            container.append(card)
    ranks = []
    for item in container:  # Get ranks of each card, to check for straight
        ranks.append(get_rank(item))
    ranks = sorted(ranks)  # Place ranks in increasing order
    return ranks[-1]


def give_sorted_flags(flags):
    return sorted(flags)


def create_counter(list):
    cnt = Counter()
    for element in sorted(list, reverse=True):
        cnt[element] += 1
    return cnt



def sort_backwards(list):
    """
        Should give a list such as: [1, 8, 2, 2, 3, 5, 7, 5, 7,9,9,9]
        Will return a sorted list of sort: [9, 9, 9, 7, 7, 5, 5, 2, 2, 8, 3, 1]
    """
    se = [[None, [None]]]
    cnt = create_counter(list)
    for key, value in cnt.items():
        count = 0
        done = False
        for index in se:
            if index[0] == value:
                se[count][1].append(key)
                done = True
                break
            else:
                count += 1
                continue
        if done:
            continue
        elif not done:
            se.append([value, [key]])
    se.__delitem__(0)
    se.sort(reverse=True)
    count = 0
    for i in se:
        se[count][1].sort(reverse=True)
        count += 1

    li = []
    for matches in se:
        for num in sorted(matches[1], reverse=True):
            for times in range(matches[0]):
                li.append(num)
    return li


def choose_winner(results):
    if results[0] > results[1]:
        return 1
    elif results[0] < results[1]:
        return 2
    else:
        return 0


def do(firsthand, secondhand):
    results = play(firsthand, secondhand)
    if choose_winner(results) == 1:
        return 1
    elif choose_winner(results) == 2:
        return 2
    else:
        return 0


for hand in hands:
    hand = hand.split(" ")
    firsthand = []
    secondhand = []
    cardcount = 0
    for card in hand:
        cardcount += 1
        if cardcount <= 5:
            firsthand.append(card)
        else:
            secondhand.append(card)
    winner = do(firsthand, secondhand)
    if winner == 1:
        player1wins += 1
    elif winner == 2:
        player2wins += 1
    else:
        print(winner, firsthand, secondhand, do(firsthand, secondhand))

print("Player 1 Wins: %s \nPlayer 2 Wins: %s\nDraws: %s (There shouldn't be any)" % (player1wins, player2wins, draws))
# The most challenging problem yet
# Answer: 376