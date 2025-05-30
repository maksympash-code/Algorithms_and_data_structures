alphabet: list[str]
N: int
k: int
count: int = 0

def solve(word: str):
    global count
    if len(word) == N:
        count += 1
        return word

    for c in alphabet:
        if c in word:
            continue
        res = solve(word + c)
        if count == k:
            return res

if __name__ == "__main__":
    N, k = map(int, input().split())

    alphabet = [chr(ord("a") + i) for i in range(N)]
    print(solve(""))