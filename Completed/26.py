def is_repetitive(num):
    val = 1 / 7
    end = list(str(val))[2:]
    for i in range(1, 10):
        first = []
        match = []
        for j in range(0, i):
            first.append(end[j])
        for k in range(i, i + i):
            match.append(end[k])
        if first == match:
            y = None
            for x in range(0, len(first)):
                if first[x] == y:
                    print(first, match)
                    return False
                y = first[x]
            return len(first)
    return False


from decimal import *

context = getcontext()
context.prec = 2000
# print(Decimal(1) / Decimal(7))

def get_rep(n, g):
    if str(n)[-1] == ".":
        return 0
    # print(str(n))
    last = str(n).split(".")[1]
    if len(last) * 2 < g:
        return 0
    for i in range(5, 1000):
        # print("%s, \n, %s, \n %s" % (last[:i], last, i))
        for j in range(0, len(last)):
            if last[j:j+i] == last[j+i:j+i*2]:
                length = i
                # print("%s, \n %s, %s" % (last[:i], last, length))
                # print("l = %s" %length)
                return length
    return 0

# for i in range(1, 11):
#     print(is_rep(1/i))
# is_rep(1/7)
# print(1 / 7, 1 / 9)
greatest = 0
val = 0
for d in range(2, 1001):
    if d % 100 == 0:
        print("At %s" % d)
    # print("?")
    rep_length = get_rep(Decimal(1)/ Decimal(d), greatest)
    if rep_length > greatest:
        greatest = rep_length
        val = d

print("Val: " + str(val) + ", Greatest: " + str(greatest))
# Answer: 983
