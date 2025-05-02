class Graph:
    def __init__(self, n, mat):
        self.n = n
        self.mat = mat

    def dfs(self, u, visited):
        visited[u] = True
        count = 1

        for v in range(self.n):
            if self.mat[u][v] == 1 and not visited[v]:
                count += self.dfs(v, visited)

        return count

    def component_size(self, start):
        visited = [False] * self.n

        return self.dfs(start, visited)


if __name__ == '__main__':
    n , s = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    g = Graph(n, matrix)
    print(g.component_size(s - 1))
