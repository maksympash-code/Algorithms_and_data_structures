# Найперше входження елемента
def bsearch_leftmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        else:
            right = m
    return left

array = [1, 1, 1, 3, 3, 5, 5, 6, 6, 6, 7]
x = 8

print(bsearch_leftmost(array, x))