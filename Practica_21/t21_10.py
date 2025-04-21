class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentMatrix = [[0] * self.mVertexNumber for _ in range(self.mVertexNumber)]

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentMatrix[source][destination] = weight
        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][source] = weight

    def degrees(self):
        return [sum(row) for row in self.mAdjacentMatrix]


if __name__ == '__main__':
    n = int(input())
    graph = Graph(oriented=False, vertex_number=n)

    for i in range(n):
        row = input().split()
        for j, val in enumerate(row):
            if val == '1':
                graph.addEdge(i, j)

    degs = graph.degrees()
    print(*degs)