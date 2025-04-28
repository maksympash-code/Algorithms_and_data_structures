from collections import deque

class Graph:
    def __init__(self, oriented=False, v=0, matrix=None):
        self.oriented = oriented
        self.v = v
        if matrix is not None:
            self.graph = matrix
        else:
            self.graph = [[0] * v for _ in range(v)]

    def bfs(self, start, finish):
        n = self.v
        distances = [-1] * n
        distances[start] = 0

        queue = deque([start])
        while queue:
            u = queue.popleft()
            if u == finish:
                return distances[u]
            for v in range(n):
                if self.graph[u][v] and distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        return 0

if __name__ == '__main__':
    n, s, f = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    g = Graph(oriented=False, v=n, matrix=mat)
    dist = g.bfs(s-1, f-1)
    print(dist)
