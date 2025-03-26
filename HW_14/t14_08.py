class Queue:
    def __init__(self, maxsize=100):
        self._items = [None for _ in range(maxsize)]
        self._front = 0
        self._back = 0
        self._size = 0

    def push(self, item):
        if self._size > 0:
            self._back = (self._back + 1) % len(self._items)
        self._items[self._back] = item
        self._size += 1
        return "ok"

    def pop(self):
        item = self._items[self._front]
        self._size -= 1
        if self._size > 0:
            self._front = (self._front + 1) % len(self._items)
        return item

    def front(self):
        return self._items[self._front]

    def size(self):
        return self._size

def solve():
    while True:
        line = input().strip()
        if not line:
            continue
        n, m, k = map(int, line.split())
        if n == 0 and m == 0 and k == 0:
            break
        total = n + m
        queue = Queue(total + 10)
        for _ in range(n):
            queue.push("G")
        for _ in range(m):
            queue.push("K")
        while queue.size() > 1:
            for _ in range(k - 1):
                queue.push(queue.pop())
            first = queue.pop()
            for _ in range(k - 1):
                queue.push(queue.pop())
            second = queue.pop()
            if first == second:
                new_maid = "G"
            else:
                new_maid = "K"
            queue.push(new_maid)
        last = queue.pop()
        print("Gared" if last == "G" else "Keka")

if __name__ == '__main__':
    solve()
