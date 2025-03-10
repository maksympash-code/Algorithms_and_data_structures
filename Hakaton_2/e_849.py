def partitions(n, min_val):
    if n == 0:
        yield []
    for i in range(min_val, n + 1):
        for tail in partitions(n - i, i):
            yield [i] + tail


if __name__ == '__main__':
    N = int(input())
    parts = [p for p in partitions(N, 1) if len(p) > 1]
    parts.sort(key=lambda p: (p[0], -p[-1], len(p), p))
    for p in parts:
        print("+".join(map(str, p)))