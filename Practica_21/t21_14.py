class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentMatrix = [[0] * self.mVertexNumber for _ in range(self.mVertexNumber)]

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentMatrix[source - 1][destination - 1] = weight

    def setMatrix(self, matrix):
        self.mVertexNumber = len(matrix)
        self.mAdjacentMatrix = matrix

    def sources(self):
        sources = []
        for j in range(self.mVertexNumber):
            if all(self.mAdjacentMatrix[i][j] == 0 for i in range(self.mVertexNumber)):
                sources.append(j + 1)
        return sources

    def sinks(self):
        sinks = []
        for i in range(self.mVertexNumber):
            if all(self.mAdjacentMatrix[i][j] == 0 for j in range(self.mVertexNumber)):
                sinks.append(i + 1)
        return sinks

if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    graph = Graph(oriented=True, vertex_number=n)
    graph.setMatrix(matrix)
    src = graph.sources()
    snk = graph.sinks()
    print(len(src), *src)
    print(len(snk), *snk)