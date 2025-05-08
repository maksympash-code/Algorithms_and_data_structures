from collections import deque

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def wave(maze, R, C):
    # Визначаємо координати точок (g, l, e)
    for i in range(R):
        for j in range(C):
            ch = maze[i][j]
            if ch == 'g':
                gi, gj = i, j
            elif ch == 'l':
                li, lj = i, j
            elif ch == 'e':
                ei, ej = i, j

    # BFS для Лі Чака
    visited_L = [[-1]*C for _ in range(R)]
    dq = deque([(li, lj)])
    visited_L[li][lj] = 0

    while dq:
        i, j = dq.popleft()
        d_L = visited_L[i][j]
        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C:
                if maze[ni][nj] != 'R' and maze[ni][nj] != 'e'and visited_L[ni][nj] == -1:
                    visited_L[ni][nj] = d_L + 1
                    dq.append((ni, nj))

    # якщо Чак вже на g у 0-й крок — негайно NO
    if visited_L[gi][gj] == 0:
        print("NO")
        return

    # BFS для Гайбраша
    visited_G = [[-1]*C for _ in range(R)]
    dq = deque([(gi, gj)])
    visited_G[gi][gj] = 0
    safe = False

    while dq:
        i, j = dq.popleft()
        d_G = visited_G[i][j]
        if (i, j) == (ei, ej):
            safe = True
            break
        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj
            nd = d_G + 1
            if 0 <= ni < R and 0 <= nj < C:
                if maze[ni][nj] != 'R':
                    if (visited_L[ni][nj] == -1 or nd < visited_L[ni][nj]) and visited_G[ni][nj] == -1 and nd <= 1000:
                        visited_G[ni][nj] = nd
                        dq.append((ni, nj))

    print("YES" if safe else "NO")


if __name__ == '__main__':
    k = int(input())
    for _ in range(k):
        R, C = map(int, input().split())
        maze = [list(input()) for _ in range(R)]
        wave(maze, R, C)
