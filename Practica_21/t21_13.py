class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number
        self.mAdjacentMatrix = [[0] * self.mVertexNumber for _ in range(self.mVertexNumber)]

    def setMatrix(self, matrix):
        self.mVertexNumber = len(matrix)
        self.mAdjacentMatrix = matrix

    def isSimpleUndirected(self):
        for i in range(self.mVertexNumber):
            if self.mAdjacentMatrix[i][i] != 0:
                return False
            for j in range(i + 1, self.mVertexNumber):
                if self.mAdjacentMatrix[i][j] != self.mAdjacentMatrix[j][i]:
                    return False
                if self.mAdjacentMatrix[i][j] not in (0, 1):
                    return False
        return True

if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    graph = Graph(oriented=False, vertex_number=n)
    graph.setMatrix(matrix)
    print("YES" if graph.isSimpleUndirected() else "NO")