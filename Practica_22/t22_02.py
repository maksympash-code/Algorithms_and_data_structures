from collections import deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.mat = [[] for _ in range(n)]

    def addEdge(self, u, v):
        self.mat[u].append(v)
        self.mat[v].append(u)

    def short_path(self, s, f):
        distance = [-1] * self.n
        p = [-1] * self.n

        dq = deque([s])
        distance[s] = 0

        while dq:
            u = dq.popleft()
            if u == f:
                break

            for w in self.mat[u]:
                if distance[w] == -1:
                    distance[w] = distance[u] + 1
                    p[w] = u
                    dq.append(w)

        if distance[f] == -1:
            return None

        path = []
        current = f

        while current != -1:
            path.append(current)
            current = p[current]

        path.reverse()
        return path


if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b = map(int, input().split())

    a, b = a - 1, b - 1

    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.addEdge(u - 1, v - 1)

    path = g.short_path(a, b)
    if not path:
        print(-1)
    else:
        l = len(path) - 1
        print(l)
        print(*[x + 1 for x in path])
