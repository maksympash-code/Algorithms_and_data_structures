class Graph:
    def __init__(self, oriented=True, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentMatrix = [[0] * self.mVertexNumber for _ in range(self.mVertexNumber)]

    def addEdge(self, source, destination):
        self.mAdjacentMatrix[source - 1][destination - 1] = 1

    def printMatrix(self):
        for row in self.mAdjacentMatrix:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = Graph(oriented=True, vertex_number=n)
    for _ in range(m):
        u, v = map(int, input().split())
        graph.addEdge(u, v)
    graph.printMatrix()
