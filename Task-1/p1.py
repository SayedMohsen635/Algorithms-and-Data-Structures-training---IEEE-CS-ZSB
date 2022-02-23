# Method to calculate the points which we got in the game
def calcPoints(D):
    if(D <= 800):
        result = 1
    if(800 < D <= 1400):
        result = 2
    if(1400 < D <= 2000):
        result = 3
    return result
    
# Program Test
distance = int(input())
print(calcPoints(distance))