class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0


    def insert(self, key):
        self.size += 1
        self.heap.append(key)
        self.siftUp()

    def siftUp(self):
        i = self.size

        while i > 1:
            parent = i // 2

            if self.heap[i] < self.heap[parent]:
                self.swap(i, parent)
            else:
                break
            i = parent

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j] , self.heap[i]

    def extractMin(self):
        minimum = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.siftDown()
        return minimum

    def siftDown(self):
        i = 1

        while 2 * i <= self.size:
            left = 2 * i
            right = left + 1
            min_child = left

            if right <= self.size and self.heap[right] < self.heap[left]:
                min_child = right
            if self.heap[i] > self.heap[min_child]:
                self.swap(i, min_child)
            else:
                break
            i = min_child

if __name__ == '__main__':
    n = int(input().strip())
    numbers = list(map(int, input().split()))
    heap = Heap()

    for num in numbers:
        heap.insert(num)

    _sum = 0
    while heap.size > 1:
        a = heap.extractMin()
        b = heap.extractMin()
        s = a + b
        _sum += s
        heap.insert(s)

    print(_sum)
