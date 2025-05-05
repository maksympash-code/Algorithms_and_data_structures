from collections import deque

class Graph:
    def __init__(self, n, matrix):
        self.n = n
        self.mat = [[]for _ in range(n)]
        self.indegree = [0] * n

        for u in range(n):
            for v in range(n):
                if matrix[u][v] == 1:
                    self.mat[u].append(v)
                    self.indegree[v] += 1

    def topological_sort(self):
        dq = deque(i for i in range(self.n) if self.indegree[i] == 0)
        counter = 0

        while dq:
            u = dq.popleft()
            counter += 1
            for v in self.mat[u]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    dq.append(v)

        return counter < self.n

if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    g = Graph(n, matrix)
    print(1 if g.topological_sort() else 0)
