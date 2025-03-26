def solve():
    with open("input.txt", "r") as f:
        first_line = f.readline().strip()
        parts = first_line.split()
        N = int(parts[0])
        M = int(parts[1])
        pattern = "".join(line.strip() for line in f)
    open_count = pattern.count("(")
    close_count = pattern.count(")")
    magic_count = pattern.count("]")
    if magic_count != M:
        M = magic_count
    net = open_count - close_count
    if net < M:
        print(0)
        return
    extra = net - M
    magic_assignments = [1] * M
    if M > 0:
        magic_assignments[-1] += extra
    balance = 0
    magic_index = 0
    for ch in pattern:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
        elif ch == "]":
            balance -= magic_assignments[magic_index]
            magic_index += 1
        if balance < 0:
            print(0)
            return
    if balance != 0:
        print(0)
        return
    print(1)
    for num in magic_assignments:
        print(num)

if __name__ == '__main__':
    solve()
