from collections import deque

EMPTY  = '.'
PAWN   = 'P'
START  = 'S'
FINISH = 'F'

DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

def min_rook_moves(maze, n, m):
    for i in range(n):
        for j in range(m):
            if maze[i][j] == START:
                si, sj = i, j
            elif maze[i][j] == FINISH:
                fi, fj = i, j

    dist = [[-1] * m for _ in range(n)]
    dq = deque()
    dist[si][sj] = 0
    dq.append((si, sj))

    while dq:
        i, j = dq.popleft()
        d0 = dist[i][j]
        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj
            while 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != PAWN:
                if dist[ni][nj] == -1:
                    dist[ni][nj] = d0 + 1
                    dq.append((ni, nj))
                else:
                    break
                ni += di
                nj += dj

    return dist[fi][fj]


if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(input().rstrip('\n')) for _ in range(n)]
    print(min_rook_moves(maze, n, m))
