size = int(input())
arr = list(map(int , input().split()))
Sereja = 0
Dima = 0
for i in range(size):
    if(arr[-1] > arr[0]):
        Sereja += arr[-1]
        arr.pop(-1)
    else:
        Sereja += arr[0]
        arr.pop(0)
    if(len(arr) == 0):
        break
    if(arr[-1] > arr[0]):
        Dima += arr[-1]
        arr.pop(-1)
    else:
        Dima += arr[0]
        arr.pop(0)
    if(len(arr) == 0):
        break
print("{:d} {:d}".format(Sereja , Dima))