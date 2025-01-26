import time

def trib(n):
    t0 = 0
    t1 = t2 = 1
    for i in range(n):
        t3 = t2 + t1 + t0
        t0 = t1
        t1 = t2
        t2 = t3
    return t0



def tribr(k):
    if k == 0:
        return 0
    elif k == 1 or k == 2:
        return 1
    else:
        tribr(k - 1) + tribr(k - 2) + tribr(k -3)

if __name__ == '__main__':
    n = 10
    s = time.time()
    trib(n)
    print(time.time() - s)
    tribr(n)
    print(time.time() - s)

