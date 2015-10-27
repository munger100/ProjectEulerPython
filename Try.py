from collections import Counter

list = [1, 3, 3, 4, 4, 8, 9, 9, 9, 7, 7]


def create_counter(list):
    """
    Creates a Counter Dictionary in form [3: 1, 2:1, 6: 2, 7: 2], unordered
    """
    cnt = Counter()
    for element in sorted(list, reverse=True):
        cnt[element] += 1
    return cnt


def sort_backwards(list):
    """
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


print(sort_backwards(list))
