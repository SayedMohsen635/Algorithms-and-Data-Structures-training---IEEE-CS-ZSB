size = int(input())
total = []
if(size != 0):
    if(size % 2 == 0):
        maxCoders = (size * size // 2)
    else:
        maxCoders = ((size * ((size//2) + 1)) - (size // 2))
    for piece in range(0 , size):
        rows = []
        for row in range(0 , size):
            if ((piece + row) % 2) == 0:
                rows.append("C")
            else:
                rows.append(".")
        total.append(rows)
    print(maxCoders)
    for i in total:
        print(*i , sep="")