from collections import deque

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def wave(n, m, cells):
    grid = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    max_size = 0

    for i in range(n):
        for j in range(m):
            if (i, j) in cells:
                grid[i][j] = 1

    for si in range(n):
        for sj in range(m):
            if grid[si][sj] == 1 and not visited[si][sj]:
                size = 0
                dq = deque()
                dq.append((si, sj))
                visited[si][sj] = True

                while dq:
                    i, j = dq.popleft()
                    size += 1
                    for di, dj in DIRECTIONS:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1 and not visited[ni][nj]:
                            visited[ni][nj] = True
                            dq.append((ni, nj))

                max_size = max(max_size, size)

    return max_size





if __name__ == '__main__':
    n, m, k = map(int, input().split())
    cells = []
    for _ in range(k):
        a, b = map(int, input().split())
        cells.append((a - 1, b - 1))

    print(wave(n, m, cells))