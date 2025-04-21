class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentMatrix = [[0] * self.mVertexNumber for _ in range(self.mVertexNumber)]

    def addEdge(self, source, destination, weight=1):
        self.mAdjacentMatrix[source - 1][destination - 1] = weight
        if not self.mIsOriented:
            self.mAdjacentMatrix[destination - 1][source - 1] = weight

    def isRegular(self):
        degrees = [sum(row) for row in self.mAdjacentMatrix]
        return all(deg == degrees[0] for deg in degrees)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = Graph(oriented=False, vertex_number=n)
    for _ in range(m):
        u, v = map(int, input().split())
        graph.addEdge(u, v)
    print("YES" if graph.isRegular() else "NO")
