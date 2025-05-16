"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шляху між двома заданими вузлами цього графа
"""

from PriorityQueue import PriorityQueue

graph: list
def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global graph
    graph = [{} for  _ in range(vertices)]


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    graph[source][destination] = weight


def getWay(start, end):
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    n = len(graph)
    INF = float('inf')
    dist = [INF] * n
    prev = [None] * n

    dist[start] = 0
    pq = PriorityQueue()
    pq.insert(start, 0)

    while not pq.empty():
        u = pq.extractMinimum()
        d_u = dist[u]
        if d_u == INF:
            break
        if u == end:
            break

        for v, w in graph[u].items():
            nd = d_u + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                if v in pq:
                    pq.updatePriority(v, nd)
                else:
                    pq.insert(v, nd)


    if dist[end] == INF:
        return []

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path
