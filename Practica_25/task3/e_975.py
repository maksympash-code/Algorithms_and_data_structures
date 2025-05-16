INF = float('inf')

def Floyd(n, matrix):
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == -1:
                matrix[i][j] = INF


    for k in range(n):
        for i in range(n):
            if matrix[i][k] == INF:
                continue
            for j in range(n):
                nd = matrix[i][k] + matrix[k][j]
                if nd < matrix[i][j]:
                    matrix[i][j] = nd

    ans = 0
    for i in range(n):
        for j in range(n):
            d = matrix[i][j]
            if d < INF and d > ans:
                ans = d

    return ans


if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(Floyd(n, matrix))