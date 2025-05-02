class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[] for _ in range(n)]

    def addEdge(self, u, v):
        self.matrix[u].append(v)
        self.matrix[v].append(u)

    def is_connected(self):
        visited = [False] * self.n
        stack = [0]
        visited[0] = True
        count = 1

        while stack:
            u = stack.pop()
            for v in self.matrix[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    count += 1
        return count == self.n


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        g.addEdge(u - 1, v - 1)

    print('YES' if g.is_connected() else 'NO')
