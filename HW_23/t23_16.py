from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.radj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.radj[v].append(u)

    def count_scc(self):
        visited = [False] * self.n
        order = []

        def dfs(u):
            visited[u] = True
            for w in self.adj[u]:
                if not visited[w]:
                    dfs(w)
            order.append(u)

        for u in range(self.n):
            if not visited[u]:
                dfs(u)

        visited = [False] * self.n
        count = 0

        def dfs_rev(u):
            visited[u] = True
            for w in self.radj[u]:
                if not visited[w]:
                    dfs_rev(w)

        for u in reversed(order):
            if not visited[u]:
                dfs_rev(u)
                count += 1

        return count

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)

    print(g.count_scc())
