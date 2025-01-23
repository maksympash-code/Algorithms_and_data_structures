def bsearch_rightmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] <= x:
            left = m + 1
        else:
            right = m
    return left - 1

array = [1, 1, 1, 3, 3, 5, 5, 6, 6, 6, 7]
x = 0

print(bsearch_rightmost(array, x))