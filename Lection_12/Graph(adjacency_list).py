class VertexBase:
    def __init__(self, key):
        self.mKey = key
        self.mData = None

    def key(self):
        return self.mKey

    def setData(self):
        pass
    def data(self):
        pass


class Vertex(VertexBase):
    def __init__(self, key):
        super().__init__(key)
        self.mNeighbours = {}

    def addNeighbour(self, vertex, weight=1):
        if isinstance(vertex, VertexBase):
            self.mNeighbours[vertex.key()] = weight
        else:
            self.mNeighbours[vertex] = weight

    def neighbours(self):
        return self.mNeighbours.keys()

    def weight(self, neighbor):
        if isinstance(neighbor, VertexBase):
            return self.mNeighbours[neighbor.key()]
        else:
            return self.mNeighbours[neighbor]


class Graph:
    def __init__(self, oriented=False):
        self.mIsOriented = oriented
        self.mVertexNumber = 0
        self.mVertices = {}


    def addVertex(self, vertex):
        if vertex in self:
            return False

        new_vertex = Vertex(vertex)
        self.mVertices[vertex] = new_vertex
        self.mVertexNumber += 1
        return True

    def getVertex(self, vertex):
        pass

    def vetices(self):
        return self.mVertices

    def addEdge(self, sourse, destination, weight=1):
        if sourse not in self:
            self.addVertex(sourse)
        if destination not in self:
            self.addVertex(destination)

        self[sourse].addNeighbor(destination, weight)

        if not self.mIsOriented:
            self[destination].addNeighbor(sourse, weight)