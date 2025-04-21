class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentMatrix = [[0] * self.mVertexNumber for _ in range(self.mVertexNumber)]

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentMatrix[source - 1][destination - 1] = weight

    def isSemicomplete(self):
        for i in range(self.mVertexNumber):
            for j in range(i + 1, self.mVertexNumber):
                if not (self.mAdjacentMatrix[i][j] or self.mAdjacentMatrix[j][i]):
                    return False
        return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = Graph(oriented=True, vertex_number=n)
    for _ in range(m):
        u, v = map(int, input().split())
        graph.addEdge(u, v)
    print("YES" if graph.isSemicomplete() else "NO")
