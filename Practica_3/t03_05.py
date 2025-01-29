def solve(arr, a, b):
     # print(arr, a , b)
    pass


if __name__ == '__main__':
    f = open('t03_05.txt')
    while f.readline():
        arr = [int(x) for x in f.readline().split()]
        a, b = [int(x) for x in f.readline().split()]
        # print(solve(arr, a, b))
    f.close()