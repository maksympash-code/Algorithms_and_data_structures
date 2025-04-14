class Heap:
    def __init__(self, items):
        self.heap = [0] + items
        self.size = len(items)

    def is_heap(self):
        for i in range(1, self.size + 1):
            left = 2 * i
            right = left + 1

            if left  <= self.size and self.heap[i] > self.heap[left]:
                return False
            if right <= self.size and self.heap[i] > self.heap[right]:
                return False
        return True

if __name__ == '__main__':
    n = (int(input().strip()))
    array = list(map(int, input().split()))
    heap = Heap(array)
    print('YES' if heap.is_heap() else 'NO')