
def solve(i, left, right):
    if i == m:
        if left == right:
            res.add(left)
        return

    solve(i + 1, left, right)
    solve(i + 1, left + plates[i], right)
    solve(i + 1, left, right + plates[i])


if __name__ == '__main__':
    n, m = map(int, input().split())
    buckets = list(map(int, input().split()))
    plates = list(map(int, input().split()))
    res = set()
    solve(0, 0, 0)

    ans = set()
    for b in buckets:
        for s in res:
            ans.add(b + 2 * s)
    for weight in sorted(ans):
        print(weight)
