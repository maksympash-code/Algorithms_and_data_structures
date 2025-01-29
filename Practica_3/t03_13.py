def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l + 1) // 2
        if arr[m] < x:
            r = m - 1
        else:
            l = m
    return l



if __name__ == '__main__':
    a = [12, 11, 11, 10, 8, 7, 7, 3, 3, 2, 2, 1, 0, 0]
    x = 2
    i = binary_search(a, x)
    print(i)