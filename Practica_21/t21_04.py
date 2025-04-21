class Graph:
    def __init__(self, oriented=True, vertex_number = 20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number

        self.mAdjacentMatrix = []

        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def addEdge(self, source, destination, weight = 1):
        self.mAdjacentMatrix[source][destination] = weight

        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][source] = weight

    def setMatrix(self, matrix):
        self.mVertexNumber = len(matrix)
        self.mAdjacentMatrix = matrix

    def countEdges(self):
        count = 0
        for i in range(self.mVertexNumber):
            for j in range(self.mVertexNumber):
                if self.mAdjacentMatrix[i][j] == 1:
                    count += 1
        return count


if __name__ == '__main__':
    n = int(input())
    graph = Graph(oriented=True, vertex_number=n)

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph.setMatrix(matrix)

    print(graph.countEdges())