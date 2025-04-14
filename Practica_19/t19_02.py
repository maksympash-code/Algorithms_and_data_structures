def heapSort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        siftDown(array, i, n)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        siftDown(array, 0, i)

def siftDown(array, start, end):
    while True:
        left = start * 2 + 1
        right = left + 1
        largest = start

        if left < end and array[left] > array[largest]:
            largest = left
        if right < end and array[right] > array[largest]:
            largest = right
        if largest == start:
            break

        array[start], array[largest] = array[largest], array[start]
        start = largest

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    heapSort(arr)
    print(*arr)