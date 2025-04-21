class SegmentTree:
    def __init__(self, data):
        self.n0 = len(data)
        size = 1
        while size < self.n0:
            size <<= 1
        self.n = size
        self.tree = [0] * (2 * self.n)
        for i, v in enumerate(data):
            self.tree[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def update(self, pos, value):
        i = pos + self.n
        self.tree[i] = value
        i //= 2
        while i:
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]
            i //= 2

    def find_prefix(self, cap):
        if self.tree[1] <= cap:
            return self.n0
        idx = 1
        while idx < self.n:
            left_sum = self.tree[2*idx]
            if left_sum > cap:
                idx = 2*idx
            else:
                cap -= left_sum
                idx = 2*idx + 1
        return idx - self.n

if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))
    m = int(input())
    st = SegmentTree(weights)
    answers = []
    for _ in range(m):
        parts = input().split()
        t = int(parts[0])
        if t == 1:
            v = int(parts[1])
            cnt = st.find_prefix(v)
            answers.append(str(cnt))
        else:
            x = int(parts[1]) - 1
            y = int(parts[2])
            st.update(x, y)
    print("\n".join(answers))
