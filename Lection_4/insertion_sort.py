

def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        currentValue = array[index]
        position = index

        while position > 0:
            if array[position] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue