def bsearch(arr, x):
    return _bsearch(arr, 0, len(arr) - 1, x)

def _bsearch(arr, l, r, x):
    if l == r:
        return l

    m = l + (r - l) // 2
    if arr[m] < x:
        return _bsearch(arr, m + 1, r, x)
    else:
        return _bsearch(arr, l, m, x)


if __name__ == '__main__':
    a = [0, 0, 1, 2, 2, 3, 3, 7, 7, 8, 10, 11, 11, 12]
    x = 2
    i = bsearch(a, x)
    print(i)