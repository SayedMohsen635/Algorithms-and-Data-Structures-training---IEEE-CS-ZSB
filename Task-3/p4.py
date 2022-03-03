st = list(input())
inst = list(input())
position = 0
for i in inst:
    if(st[position] == i):
        position += 1
lastPosition = position + 1
print(lastPosition)