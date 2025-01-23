def binary_continuous(f, c, a, b):
    l = a
    r = b

    m = (l + r) / 2.0
    while l != m and m != r:
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return l