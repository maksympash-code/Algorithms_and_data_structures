class Graph:
    def __init__(self, oriented = False, vertex_number = 20):

        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number

        # Створюємо матрицю суміжності заповнену нулями
        self.mAdjacentMatrix = []
        for i in range(self.mVertexNumber):
            self.mAdjacentMatrix.append([0] * self.mVertexNumber)


    def addEdge(self, sourse, destination, weight = 1):
        self.mAdjacentMatrix[sourse][destination] = weight

        if not self.mIsOriented:
            self.mAdjacentMatrix[destination][sourse] = weight
    