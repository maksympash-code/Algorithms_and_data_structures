# Перший метод
def binary_search(array, x):
    left = 0 # Індех лівого елементу
    right = len(array) - 1 # Індех правого елементу
    while left < right:
        m = (left + right) // 2 # Індех середнього елементу
        if array[m] < x:
            left = m + 1
        else:
            right = m

    return array[right] == x
