class Heap:
    def __init__(self):
        self.mItems = [0]
        self.mSize = 0


    def insert(self, key):
        self.mSize += 1
        self.mItems.append(key)
        self.siftUp()

    def siftUp(self):
        i = self.mSize

        while i > 1:
            parent = i // 2

            if self.mItems[i] > self.mItems[parent]:
                self.swap(i, parent)
            else:
                break
            i = parent

    def swap(self, i, j):
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def extract(self):
        maximum = self.mItems[1]
        self.mItems[1] = self.mItems[self.mSize]
        self.mItems.pop()
        self.mSize -= 1
        self.siftDown()
        return maximum

    def siftDown(self):
        i = 1

        while 2 * i <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            max_child = self.maxChild(left, right)

            if self.mItems[i] < self.mItems[max_child]:
                self.swap(i, max_child)
            else:
                break
            i = max_child

    def maxChild(self, left, right):
        if right > self.mSize:
            return left
        return left if self.mItems[left] >= self.mItems[right] else right


if __name__ == '__main__':
    n = int(input().strip())
    heap = Heap()
    output = []

    for _ in range(n):
        parts = input().split()
        if parts[0] == '0':
            heap.insert(int(parts[1]))
        elif parts[0] == '1':
            output.append(str(heap.extract()))

    print('\n'.join(output))


