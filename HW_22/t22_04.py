from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def addEdge(self, s, d):
        self.graph[s].append(d)
        self.graph[d].append(s)

    def bfs(self, sourses):
        dist = [-1] * self.n
        dq = deque()
        for s in sourses:
            dist[s] = 0
            dq.append(s)

        while dq:
            u = dq.popleft()
            for v in self.graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    dq.append(v)

        maxd = max(dist)
        last = min(i for i, d in enumerate(dist) if d == maxd)
        return maxd, last



if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        g.addEdge(u - 1, v - 1)

    k = int(input())
    sourses = [x - 1 for x in map(int, input().split())]

    time, last = g.bfs(sourses)
    print(time)
    print(last + 1)