n = int(input())
status = False
arr = []
count = 0
for i in range(n):
    seats = list(input())
    if(''.join(seats[0 : 2]) == "OO"):
        if(status == True):
            arr.append(seats)
        else:
            seats[0 : 2] = ["++"]
            arr.append(seats)
            status == True
        count += 1
    elif(''.join(seats[3:]) == "OO"):
        if(status == True):
            arr.append(seats)
        else:
            seats[3:] == ["++"]
            arr.append(seats)
            status == True
        count += 1
    else:
        arr.append(seats)
if(count == 0):
    print("NO")
else:
    print("YES")
    for i in arr:
        print("".join(i))
