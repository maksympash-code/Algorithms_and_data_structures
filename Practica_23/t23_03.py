class Graph:
    def __init__(self, n, mat):
        self.n = n
        self.mat = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if mat[i][j] == 1:
                    self.mat[i].append(j)

    def count_components(self):
        visited = [False] * self.n
        components = 0

        for i in range(self.n):
            if not visited[i]:
                components += 1

                stack = [i]
                visited[i] = True

                while stack:
                    u = stack.pop()
                    for v in self.mat[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
        return components

if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    g = Graph(n, matrix)
    print(g.count_components())