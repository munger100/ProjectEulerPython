total = 0

index_array = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
               "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty",
               "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]


def get_count(str):
    count = 0
    for i in str:
        count += 1
    return count


def get(int):
    return get_count(index_array[int])


for i in range(0, 18 + 1):  # Numbers 1-19
    total += get(i)
    print("%s" % index_array[i])

for i in range(19, 26 + 1):  # Numbers 20-99
    for j in range(-1, 8 + 1):
        if j == -1:
            total += get(i)
            print("%s" % index_array[i])
        else:
            total += get(i) + get(j)
            print("%s %s" % (index_array[i], index_array[j]))

print("20-99 %s" % total)  # total = 854

for i in range(0, 8 + 1):  # Numbers 100-999
    total += get(i) + get_count("hundred")
    print("%s hundred" % index_array[i])
    for l in range(0, 18 + 1):
        total += get(i) + get_count("hundred") + get_count("and") + get(l)
        print("%s hundred and %s" % (index_array[i], index_array[l]))
    for j in range(19, 26 + 1):
        for k in range(-1, 8 + 1):
            if k == -1:
                total += get(i) + get_count("hundred") + get_count("and") + get(j)
                print("%s hundred and %s" % (index_array[i], index_array[j]))
            else:
                total += get(i) + get_count("hundred") + get_count("and") + get(j) + get(k)
                print("%s hundred and %s %s" % (index_array[i], index_array[j], index_array[k]))

total += get_count("one") + get_count("thousand")  # 1000
print("one thousand")

print("Total: %s" % total)
# Answer: 21124
