class Graph:
    def __init__(self, oriented=False, vertex_number=20):
        self.mIsOriented = oriented
        self.mVertexNumber = vertex_number

        self.adjacency_lists = [set() for _ in range(self.mVertexNumber + 1)]

    def AddEdge(self, source, destination):
        self.adjacency_lists[source].add(destination)
        if not self.mIsOriented:
            self.adjacency_lists[destination].add(source)

    def Vertex(self, vertex):
        return sorted(self.adjacency_lists[vertex])


if __name__ == "__main__":
    n = int(input())
    adj = [set() for _ in range(n + 1)]
    k = int(input())

    output = []

    for _ in range(k):
        command = input().split()
        if command[0] == '1':
            u = int(command[1])
            v = int(command[2])
            adj[u].add(v)
            adj[v].add(u)
        else:
            vertex = int(command[1])
            if adj[vertex]:
                output.append(' '.join(map(str, sorted(adj[vertex]))))
            else:
                output.append('')

    print('\n'.join(output))

