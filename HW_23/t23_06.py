from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.indegree = [0] * n

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.indegree[v] += 1

    def topological_sort(self):
        q = deque()
        for i in range(self.n):
            if self.indegree[i] == 0:
                q.append(i)

        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    q.append(v)

        if len(order) < self.n:
            return None
        return order

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)

    res = g.topological_sort()
    if res is None:
        print(-1)
    else:
        print(" ".join(str(u + 1) for u in res))
