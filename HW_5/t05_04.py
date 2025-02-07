def can_cut(p, k, l):
    count = 0
    for i in p:
        count += i // l
    return count >= k

def solve(p, k):
    l = 1
    r = max(p)
    result = 0

    while l <= r:
        m = (l + r) // 2
        if can_cut(p, k, m):
            result = m
            l = m + 1
        else:
            r = m - 1
    return result
if __name__ == "__main__":
    n, k = map(int, input().split())
    p = [int(input()) for _ in range(n)]
    print(solve(p, k))