from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.list = [[] for _ in range(n)]

    def add_edge(self, u, v, idx):
        self.list[u].append((v, idx))
        self.list[v].append((u, idx))

    def is_connected(self, removed_edges, start = 0):
        vis = [False] * self.n
        vis[start] = True
        dq = deque([start])
        counter = 1
        rem = set(removed_edges)

        while dq:
            u = dq.popleft()
            for v, w in self.list[u]:
                if w in rem or vis[v]:
                    continue
                vis[v] = True
                counter += 1
                dq.append(v)
        return counter == self.n

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)
    for i in range(1, m + 1):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1, i)

    q = int(input())
    for _ in range(q):
        lst = list(map(int, input().split()))
        rem = lst[1:]
        print("Connected" if g.is_connected(rem) else "Disconnected")
