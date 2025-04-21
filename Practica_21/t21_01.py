class Graph:
    def __init__(self, oriented = False, vertex_number = 20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number

        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def addEdge(self, sourse, destination, weight = 1):
        self.mAdjacentMatrix[sourse][destination] = weight

        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][sourse] = weight

    def setMatrix(self, matrix):
        self.mVertexNumber = len(matrix)
        self.mAdjacentMatrix = matrix

    def getEdgeList(self):
        edges = []

        for i in range(self.mVertexNumber):
            for j in range(i + 1, self.mVertexNumber):
                if self.mAdjacentMatrix[i][j] == 1:
                    edges.append([i + 1, j + 1])
        return edges


if __name__ == '__main__':
    n = int(input())

    graph = Graph(oriented=False, vertex_number=n)

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph.setMatrix(matrix)

    edges = graph.getEdgeList()
    for edge in edges:
        print(f"{edge[0]} {edge[1]}")
