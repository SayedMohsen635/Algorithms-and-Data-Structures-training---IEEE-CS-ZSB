import sys

row , col = map(int , input().split())
for i in range(row):
    for x in input().split():
        if x not in ['B', 'W', 'G']:
            print('#Color')
            sys.exit()
print('#Black&White')