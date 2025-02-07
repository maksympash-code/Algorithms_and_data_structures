def can_place_cows(p, k, d):
    count = 1
    last_p = p[0]

    for pos in p[1:]:
        if pos - last_p >= d:
            count += 1
            last_p = pos
            if count == k:
                return True
    return False

def solve(p ,k):
    l = 0
    r = p[-1] - p[0]
    result = 0

    while l <= r:
        m = (l + r) // 2
        if can_place_cows(p, k, m):
            result = m
            l = m + 1
        else:
            r = m - 1
    return result


if __name__ == '__main__':
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(solve(p, k))