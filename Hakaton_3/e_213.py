from collections import deque


def solve():
    H, W = map(int, input().split())
    maze = [input().rstrip('\n') for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if maze[i][j] == '1':
                s1 = (i, j)
            elif maze[i][j] == '2':
                s2 = (i, j)
            elif maze[i][j] == '*':
                exit_cell = (i, j)

    COMMANDS = ['R', 'L', 'U', 'D']
    DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    start = (s1[0], s1[1], s2[0], s2[1])
    dq = deque([start])
    visited = {start: None}

    while dq:
        i1, j1, i2, j2 = state = dq.popleft()

        if (i1, j1) == exit_cell and (i2, j2) == exit_cell:
            path = []
            cur = state
            while visited[cur] is not None:
                prev, cmd_idx = visited[cur]
                path.append(COMMANDS[cmd_idx])
                cur = prev
            path.reverse()
            print(len(path))
            print(''.join(path))
            return

        for cmd_idx, (di, dj) in enumerate(DIRS):
            ni1, nj1 = i1 + di, j1 + dj
            if not (0 <= ni1 < H and 0 <= nj1 < W and maze[ni1][nj1] != '#'):
                ni1, nj1 = i1, j1
            ni2, nj2 = i2 + di, j2 + dj
            if not (0 <= ni2 < H and 0 <= nj2 < W and maze[ni2][nj2] != '#'):
                ni2, nj2 = i2, j2

            new_state = (ni1, nj1, ni2, nj2)
            if new_state not in visited:
                visited[new_state] = (state, cmd_idx)
                dq.append(new_state)

    print(-1)


if __name__ == "__main__":
    solve()
