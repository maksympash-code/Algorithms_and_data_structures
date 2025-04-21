class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentMatrix = [[0] * self.mVertexNumber for _ in range(self.mVertexNumber)]

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentMatrix[source][destination] = weight
        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][source] = weight

    def setMatrix(self, matrix):
        self.mVertexNumber = len(matrix)
        self.mAdjacentMatrix = matrix

    def getEdgeList(self):
        edges = []
        for i in range(self.mVertexNumber):
            for j in range(self.mVertexNumber):
                if self.mAdjacentMatrix[i][j] == 1:
                    edges.append([i + 1, j + 1])
        return edges

if __name__ == '__main__':
    n = int(input())
    graph = Graph(oriented=True, vertex_number=n)
    matrix = [list(map(int, input().split())) for _ in range(n)]
    graph.setMatrix(matrix)
    edges = graph.getEdgeList()
    edges.sort(key=lambda x: (x[0], x[1]))
    for u, v in edges:
        print(u, v)