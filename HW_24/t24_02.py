from collections import deque

START = '@'
END = 'X'

CELL = '.'
WALL = 'O'

VISITED = 1
EMPTY = 0

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def find_positions(maze, n):
    start = end = None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == START:
                start = (i, j)
            elif maze[i][j] == END:
                end = (i, j)
    return start, end


def wave(maze, n):
    visited = [[EMPTY] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    start, end = find_positions(maze, n)

    si, sj = start
    dq = deque()
    dq.append((si,sj))
    visited[si][sj] = VISITED

    while dq:
        i, j = dq.popleft()
        if (i, j) == end:
            break
        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == EMPTY and maze[ni][nj] in (CELL, END):
                visited[ni][nj] = VISITED
                parent[ni][nj] = (i, j)
                dq.append((ni, nj))

    ei, ej = end
    if visited[ei][ej] == EMPTY:
        print('N')
        return

    i, j = end
    while (i, j) != start:
        if maze[i][j] in (CELL, END):
            maze[i][j] = '+'
        i, j = parent[i][j]

    print('Y')
    for row in maze:
            print(''.join(row))




if __name__ == '__main__':
    n = int(input())
    maze = [list(input().rstrip()) for _ in range(n)]
    wave(maze, n)

