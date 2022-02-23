if __name__ == '__main__':
    time = int(input())
    avSpeed = int(input())
    distance = avSpeed * time
    print("{:.3f}".format(distance / 12))