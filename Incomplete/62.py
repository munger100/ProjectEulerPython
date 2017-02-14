from itertools import permutations

cubes = []
for i in range(0, 1000):  # Gen cubes
    cubes.append(i ** 3)
    if i % 100 == 0:
        print("Generating %s" % i)
print("Done generating")

for i in range(400,410):
    cube = cubes[i]
    idx = cubes.index(cube)
    if idx % 1   == 0:
        print("At cube #%s" % idx)
    count = 1
    used = []
    found = [cube]
    arr = []
    for perm in permutations(str(cube)):
        if perm not in arr:
            arr.append(perm)
    for a in arr:
        num = int(''.join(a))
        if '0' in a or str(cube) == num:
            continue
        if num in used or num in found:
            continue
        used.append(num)
        # print("perm = {0}".format(perm))
        if num in cubes:
            # print(num)
            found.append(num)
            print(idx, found)
            count += 1
    if count == 3:
        print(count, cubes.index(cube), found)


# cubes, used = [], []
# for i in range(1, 1000):  # Works, but too long
#     if i % 100 == 0:
#         print("i = %s" % i)
#     cube = i ** 3
#     cubes.append(cube)
#     count = 1
#     for perm in permutations(str(cube)):
#         if int(''.join(perm)) in cubes:
#             count += 1
#     if count == 3:
#         print(i)
#
