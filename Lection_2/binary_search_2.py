# Другий метод
def binary_search(array, x):
    left = 0 # Індех лівого елементу
    right = len(array) - 1 # Індех правого елементу
    while left <= right:
        m = left + (right-left) // 2 # середина відрізку # Правильний запис
        if array[m] < x:
            left = m + 1
        elif array[m] > x:
            right = m - 1
        else:
            return m

    return None
