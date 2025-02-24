"""
Проведіть аналіз швидкодії реалізованих алгоритмів сортування
для різних типів та розмірів масивів (не відсортований масив
згенерований випадковим чином, масив відсортований за зростанням,
масив відсортований за спаданням елементів).
"""

N = 5000     # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]



def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for j in range(n - 1, 0, -1):
        _sorted = True
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                _sorted = False
        if _sorted:
            return


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for j in range(n, 1, -1):
        pos = 0
        for i in range(1, j):
            if array[i] > array[pos]:
                pos = i
        array[pos], array[j - 1] = array[j - 1], array[pos]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for pos in range(1, n):
        x = array[pos]
        while pos > 0:
            if array[pos - 1] > x:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1
        array[pos] = x


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    _sort(array, 0, len(array) - 1)

def _sort(array, a, b):
    if a == b:
        return

    m = a + (b - a) // 2
    _sort(array, a, m)
    _sort(array, m + 1, b)

    left = array[a: m + 1]

    i = 0
    j = m + 1
    k = a

    while i < len(left) and j <= b:
        if left[i] < array[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1


def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    _sort_q(array, 0 , len(array) - 1)

def _sort_q(array, a, b):
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    _sort(array, a, right)
    _sort(array, right + 1, b)
