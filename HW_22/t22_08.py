from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def addEdge(self, s, d):
        self.graph[s].append(d)
        self.graph[d].append(s)

    def writing_off(self):
        color = [-1] * self.n

        for s in range(self.n):
            if color[s] != -1:
                continue
            color[s] = 0
            dq = deque([s])

            while dq:
                u = dq.popleft()
                for w in self.graph[u]:
                    if color[w] == -1:
                        color[w] = 1 - color[u]
                        dq.append(w)
                    elif color[w] == color[u]:
                        return False
        return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        g.addEdge(u - 1, v - 1)

    print('YES' if g.writing_off() else 'NO')

