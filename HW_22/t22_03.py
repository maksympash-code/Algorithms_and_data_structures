from collections import deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.mat = [[0] * n for _ in range(n)]
        self.count = 0

    def addEdge(self, s, d):
        self.mat[s][d] = 1

    def bfs(self, u, target, depth, maxd, visited):
        if depth > maxd:
            return

        if u == target:
            self.count += 1

        for v in range(self.n):
            if self.mat[u][v] and not visited[v]:
                visited[v] = True
                self.bfs(v, target, depth + 1, maxd, visited)
                visited[v] = False

    def paths(self, s, f, maxd):
        self.count = 0
        visited = [False] * self.n
        visited[s] = True
        self.bfs(s, f, 0, maxd, visited)
        return self.count


if __name__ == '__main__':
    n, k, a, b, d = map(int, input().split())
    g = Graph(n)

    for _ in range(k):
        u, v = map(int, input().split())
        g.addEdge(u - 1, v - 1)

    res = g.paths(a - 1, b - 1, d)
    print(res)