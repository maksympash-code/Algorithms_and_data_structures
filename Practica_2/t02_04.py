def f(n):
    i = n - 1
    while i != 0:
        j = 0
        while j < n: # O(n log (n))
            j += 1
        i += 1

# res: O(n log n)