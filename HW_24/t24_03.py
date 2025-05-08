from collections import deque

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def wave(maze, n, m):
    count = 0
    visited = [[False] * n for _ in range(m)]

    for si in range(m):
        for sj in range(n):
            if maze[si][sj] == '#' and not visited[si][sj]:
                count += 1

                dq = deque()
                dq.append((si, sj))
                visited[si][sj] = True

                while dq:
                    i, j = dq.popleft()
                    for di, dj in DIRECTIONS:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and maze[ni][nj] == '#':
                            visited[ni][nj] = True
                            dq.append((ni, nj))


    return count


if __name__ == '__main__':
    m, n = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(m)]

    print(wave(maze, n, m))