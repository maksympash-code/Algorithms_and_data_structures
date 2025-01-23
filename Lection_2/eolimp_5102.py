n, x, y = [int (i) for i in input().split()]
x, y = min(x, y), max(x, y)

l = 0
r = (n - 1) * y
while l < r:
    m = l + (r - 1) // 2
    k = m // x + m // y
    if k < n - 1:
        l = m + 1
    else:
        r = m

print(l + x)