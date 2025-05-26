from Practica_25.PriorityQueue import PriorityQueue

INF = float('inf')

def build_network(n, edges, dangerous):
    adj = [[] for _ in range(n)]
    min_incident = [INF] * n
    for w, u, v in edges:
        if u not in dangerous and v not in dangerous:
            adj[u].append((v, w))
            adj[v].append((u, w))
        elif u in dangerous and v not in dangerous:
            min_incident[u] = min(min_incident[u], w)
        elif v in dangerous and u not in dangerous:
            min_incident[v] = min(min_incident[v], w)

    safe = [i for i in range(n) if i not in dangerous]
    total = 0

    if not safe:
        if len(dangerous) == 1:
            return 0
        if len(dangerous) == 2:
            d0, d1 = list(dangerous)
            for w, u, v in edges:
                if {u, v} == {d0, d1}:
                    return w
        return None

    start = safe[0]
    visited = [False] * n
    dist = [INF] * n
    dist[start] = 0
    pq = PriorityQueue()
    pq.insert(start, 0)
    cnt = 0

    while not pq.empty():
        u = pq.extractMinimum()
        if visited[u]:
            continue
        visited[u] = True
        total += dist[u]
        cnt += 1
        for v, w in adj[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                if v in pq:
                    pq.updatePriority(v, w)
                else:
                    pq.insert(v, w)
    if cnt != len(safe):
        return None

    for u in dangerous:
        if min_incident[u] == INF:
            return None
        total += min_incident[u]

    return total

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    if p > 0:
        dangerous = set(int(x) - 1 for x in input().split())
    else:
        dangerous = set()
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))
    ans = build_network(n, edges, dangerous)
    print(ans if ans is not None else "impossible")

