from collections import deque


class Graph:
    def __init__(self):
        pass

    def neigbours(self, s):
        res = []

        if s[0] != '9':
            res.append(chr(ord(s[0]) + 1) + s[1:])
        if s[-1] != 1:
            res.append(s[:-1] + chr(ord(s[-1]) - 1))

        res.append(s[-1] + s[:-1])
        res.append(s[1:] + s[0])
        return res

    def path(self, s, f):
        prev = {s: None}
        dq = deque([s])

        while dq:
            u = dq.popleft()
            if u == f:
                break
            for w in self.neigbours(u):
                if w not in prev:
                    prev[w] = u
                    dq.append(w)

        if f not in prev:
            return []

        path = []
        current = f

        while current is not None:
            path.append(current)
            current = prev[current]

        path.reverse()
        return path


if __name__ == '__main__':
    start = input().strip()
    finish = input().strip()
    g = Graph()

    path = g.path(start ,finish)
    for res in path:
        print(res)