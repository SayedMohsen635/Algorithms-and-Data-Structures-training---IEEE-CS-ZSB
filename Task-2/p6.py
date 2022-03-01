n = int(input())
points = list(map(int , input().split()))
count = 0
for i in range(1 , n):
    if all([points[i] > points[j] for j in range(0 , i)]) or all([points[i] < points[j] for j in range(0 , i)]):
        count += 1
print(count)