import re, math

for n in range(1000000000, 2000000000):
    square = n ** 2
    if n % 1000000 == 0:
        print("At n = %s, square = %s" % (n, square))
    if len(str(square)) == 19:
        if re.match("1.2.3.4.5.6.7.8.9", str(n)) is not None:
            print(n, square)
#
# for i in range(0, 10):
#     j = str(i)
#     num = "1" + j + "2" + j + "3" + j + "4" + j + "5" + j + "6" + j + "7" + j + "8" + j + "9" + j + "0"
#     if math.sqrt(int(num)) % 1 == 0:
#         print(int(num), math.sqrt(int(num)))
# lol