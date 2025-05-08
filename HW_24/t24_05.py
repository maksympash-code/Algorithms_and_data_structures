from collections import deque

WALL = '#'
CELL = '.'

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def wave(maze, n):
    area = 0
    visited = [[False] * n for _ in range(n)]

    for si, sj in [(0,0), (n - 1, n - 1)]:
        if maze[si][sj] == CELL and not visited[si][sj]:
            visited[si][sj] = True
            dq = deque()
            dq.append((si, sj))
            while dq:
                i , j = dq.popleft()
                for di, dj in DIRECTIONS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] == CELL and not visited[ni][nj]:
                        visited[ni][nj] = True
                        dq.append((ni, nj))

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                for di, dj in DIRECTIONS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if maze[ni][nj] == WALL:
                            area += 9
                    else:
                        if (i, j) not in ((0, 0), (n - 1, n - 1)):
                            area += 9
    return area



if __name__ == '__main__':
    n = int(input())
    maze = [list(input().rstrip()) for _ in range(n)]

    print(wave(maze, n))