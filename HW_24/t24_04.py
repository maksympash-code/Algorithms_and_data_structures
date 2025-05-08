from collections import deque

CELL = 0
WALL = 1

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def wave(maze, n, m, si, sj, ei, ej):
    visited = [[-1] * m for _ in range(n)]

    dq = deque()
    dq.append((si, sj))

    visited[si][sj] = CELL

    while dq:
        i, j = dq.popleft()
        if (i, j) == (ei, ej):
            return visited[i][j]
        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == CELL and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1
                    dq.append((ni, nj))
    return -1




if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    print(wave(maze, n, m, y1 - 1, x1 - 1, y2 - 1, x2 - 1))