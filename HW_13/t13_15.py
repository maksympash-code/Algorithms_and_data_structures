def backtrack(seq, open_used, close_used, stack, n, half, results):
    if len(seq) == n:
        if not stack:
            results.append(seq)
        return
    if open_used < half:
        for ch in "([":
            stack.append(ch)
            backtrack(seq + ch, open_used + 1, close_used, stack, n, half, results)
            stack.pop()
    if stack:
        top = stack[-1]
        closing = ")" if top == "(" else "]"
        stack.pop()
        backtrack(seq + closing, open_used, close_used + 1, stack, n, half, results)
        stack.append(top)

def generate_expressions(n):
    half = n // 2
    results = []
    backtrack("", 0, 0, [], n, half, results)
    return results

def solve():
    n = int(input().strip())
    expressions = generate_expressions(n)
    for expr in expressions:
        print(expr)

if __name__ == '__main__':
    solve()
