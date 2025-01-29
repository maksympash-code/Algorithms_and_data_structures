# 5 -> 101
# 6 -> 110

# >> : 5 >> 1 -> 10_2 -> 2_10
# << : 5 << 1 -> 1010_2 -> 10_10
# & : 5 & 6 -> 100_2 -> 4_10
# | : 5 | 6 -> 111_2 -> 7_10
# ^ : 5 ^ 6 -> 11_2 -> 3_10
# ~


def solve(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(solve(n))