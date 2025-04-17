from math import log2

class SegmentTree:
    def __init__(self, array):

        k = len(array)
        n = (1 << int(log2(k - 1)) + 1)

        self.mItems = 2 * n * [0]

        for i in range(k):
            self.mItems[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]

        self.mSize = n - 1


    def update(self, pos, x):

        pos += self.mSize
        self.mItems[pos] += x

        i = pos // 2
        while i > 0:
            self.mItems[i] = self.mItems[2 * i] + self.mItems[2 * i + 1]
            i //= 2

    def sum(self, left, right):
        left += self.mSize
        right += self.mSize

        res = 0

        while left <= right:
            if left % 2 == 1:
                res += self.mItems[left]
            if right % 2 == 0:
                res += self.mItems[right]

            left = (left + 1) // 2
            right = (right - 1) // 2
        return res

if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    seg = SegmentTree(arr)

    for _ in range(q):
        parts = input().split()

        operation = parts[0]

        if operation == '+':
            pos = int(parts[1])
            x = int(parts[2])
            seg.update(pos, x)
        elif operation == '?':
            left = int(parts[1])
            right = int(parts[2])

            if left > right:
                left, right = right, left
            print(seg.sum(left, right))