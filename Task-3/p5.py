size = int(input())
sentence = list(input())
count = 0
if(len(sentence) == size):
    for i in range(1 , size):
        if(sentence[i] == sentence[i - 1]):
            count += 1
print(count)