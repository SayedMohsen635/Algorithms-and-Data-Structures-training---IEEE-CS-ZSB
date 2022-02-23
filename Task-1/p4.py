if __name__ == '__main__':
    N = int(input())
    for i in range(1 , 11):
        print("{:n} x {:n} = {:n}".format(i , N , N * i))