size = int(input())
lst = set(map(int , input().split()))
lst = list(lst)
answer = len(lst) - lst.count(0)
print(answer)