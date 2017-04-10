for size in range(0, 3):
    print("Size = %s" % size)
    triangles = []
    for x in range(0, size + 1):
        for y in range(0, size + 1):
            if y != x:
                triangles.append([[0,0], [])
