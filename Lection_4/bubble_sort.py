

def bubble_sort(array):
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

