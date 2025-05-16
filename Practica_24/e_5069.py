from collections import deque

def bfs(sx, sy, maze, n, m):
    dist = [[-1] * m for _ in range(n)]

    dq = deque([(sx, sy)])
    dist[sx][sy] = 0

    while dq:
        x, y = dq.popleft()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))

    return dist


if __name__ == "__main__":
    n, m = map(int, input().split())
    px, py = map(int, input().split())
    vx, vy = map(int, input().split())

    px -= 1; py -= 1
    vx -= 1; vy -= 1

    maze = [list(map(int, input().split())) for _ in range(n)]

    dist_p = bfs(px, py, maze, n, m)
    dist_v = bfs(vx, vy, maze, n, m)

    best_time = float('inf')
    best_cell = None

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 0 and dist_p[i][j] != -1 and dist_v[i][j] != -1:
                t = max(dist_p[i][j], dist_v[i][j])
                if t < best_time:
                    best_time = t
                    best_cell = (i, j)

    if best_cell is None:
        print(-1)
    else:
        print(best_cell[0] + 1, best_cell[1] + 1)
