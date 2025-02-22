class HashTable():
    def __init__(self):
        self.size = 1000003
        self.currentSize = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        current = self.hash(key)
        while self.keys[current] is not None:
            if self.keys[current] == key:
                self.values[current] = value
                return
            current = (current + 1) % self.size

        self.keys[current] = key
        self.values[current] = value
        self.currentSize += 1

    def get(self, key):
        current = self.hash(key)
        while self.keys[current] is not None:
            if self.keys[current] == key:
                return self.values[current]
            current = (current + 1) % self.size
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    ht = HashTable()
    for num in arr:
        if ht.get(num) is None:
            ht.put(num, 1)

    print(ht.currentSize)


if __name__ == '__main__':
    main()