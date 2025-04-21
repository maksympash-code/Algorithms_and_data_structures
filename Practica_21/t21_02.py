class Graph:
    def __init__(self, oriented=True, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number

        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)

    def addEdge(self, source, destination):
        self.mAdjacentMatrix[source - 1][destination - 1] = 1

    def printMatrix(self):
        for row in self.mAdjacentMatrix:
            print(" ".join(map(str, row)))

    def setFromAdjacencyList(self, adj_lists):
        for i, adj_list in enumerate(adj_lists, 1):
            num_edges = adj_list[0]
            for j in range(num_edges):
                destination = adj_list[j + 1]
                self.addEdge(i, destination)



if __name__ == "__main__":
    n = int(input())
    graph = Graph(oriented=True, vertex_number=n)

    adj_lists = []
    for _ in range(n):
        adj_list = list(map(int, input().split()))
        adj_lists.append(adj_list)

    graph.setFromAdjacencyList(adj_lists)

    graph.printMatrix()