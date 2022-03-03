games = int(input())
sentence = input()
if(len(sentence) == games):
    for i in range(games):
        if(sentence.count("A") > sentence.count("D")):
            print("Anton")
        elif(sentence.count("A") < sentence.count("D")):
            print("Danik")
        elif(sentence.count("A") == sentence.count("D")):
            print("Friendship")
        break