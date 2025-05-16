"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""

graph: list

def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графаa
    @param edges:  кількість ребер графа
    """
    global graph
    graph = [{} for _ in range(vertices)]


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    graph[source][destination] = weight


def findDistance(start, end):
    """ Знаходить довжину найкоротшого шляху, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: Довжину найкоротшого шляху або -1 якщо шляху між вершинами не існує.
    """
    n = len(graph)
    INF = float('inf')
    dist = [INF for _ in range(n)]
    dist[start] = 0

    for i in range(n - 1):
        update = False
        for j in range(n):
            if dist[j] == INF:
                continue
            for u, w in graph[j].items():
                if dist[j] + w < dist[u]:
                    dist[u] = dist[j] + w
                    update = True
        if not update:
            break

    return dist[end] if dist[end] != INF else -1


if __name__ == '__main__':
    init(6, 0)
    addEdge(0, 1, 8)
    addEdge(0, 2, 7)
    addEdge(0, 3, 2)
    addEdge(0, 4, 1)
    addEdge(1, 4, 2)
    addEdge(1, 5, 5)
    addEdge(2, 3, 3)
    addEdge(3, 2, 3)
    addEdge(3, 4, 4)
    addEdge(4, 1, 2)
    addEdge(4, 5, 10)
    print(graph)