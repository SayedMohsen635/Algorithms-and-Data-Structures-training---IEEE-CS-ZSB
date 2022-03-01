matrix = []
for i in range(5):
	matrix.append([int(i) for i in input().split(' ')])
for i in range(5):
    for k in range(5):
        if(matrix[i][k] == 1):
            counter = abs(2 - i) + abs(2 - k)
            print(counter)
            break