from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def connected_components(self):
        visited = [False] * self.n
        components = []
        for i in range(self.n):
            if not visited[i]:
                comp = []
                dq = deque([i])
                visited[i] = True
                while dq:
                    u = dq.popleft()
                    comp.append(u)
                    for w in self.adj[u]:
                        if not visited[w]:
                            visited[w] = True
                            dq.append(w)
                components.append(comp)
        return components

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)

    comps = g.connected_components()
    print(len(comps))
    for comp in comps:
        comp1 = [x + 1 for x in comp]
        print(len(comp1))
        print(" ".join(map(str, comp1)))
