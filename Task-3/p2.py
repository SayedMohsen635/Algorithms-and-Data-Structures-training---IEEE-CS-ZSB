num = int(input())
first = input().split("W")
main = []
for i in first:
    if(len(i)!=0):
        main.append(len(i))
print(len(main))
if(len(main) != 0):
    print(*main , sep = " ")