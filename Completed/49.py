from Scripts import is_prime

for t in range(0, 10000):
    if t % 1000 == 0:
        print("t = %s" % t)
    arr = []
    for i in range(0, 10000):
        # print("i = %s" % i)
        if i + 2 * t > 10000:
            # print("broke, limit")
            break
        if not is_prime(i):
            # print("broke, prime")
            continue
        arr = [i]
        for j in range(1, 3):
            i += t
            arr.append(i)
        valid = True
        dict = {}
        # print(arr)
        for a in str(arr[0]):
            dict[a] = str(arr[0]).count(a)
        # print(dict)
        for a in arr:
            if not is_prime(a):
                valid = False
            for b in str(a):
                if b not in dict:
                    valid = False
                    continue
                if int(str(a).count(b)) != dict[b]:
                    valid = False
        if arr[0] == arr[1] and arr[1] == arr[2]:
            valid = False
        if valid:
            print(valid, arr, str(arr[0]) + str(arr[1]) + str(arr[2]))
            # print(arr)
            # print(valid)

# Answer: 296962999629