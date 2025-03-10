import sys
sys.set_int_max_str_digits(10**7)

def f77(person, used_mask):
    if person == n:
        return True
    s = salaries[person]
    if s not in sum_to_masks:
        return False
    for mask in sum_to_masks[s]:
        if used_mask & mask == 0:
            if f77(person + 1, used_mask | mask):
                return True
    return False

n, m = map(int, input().split())
salaries = list(map(int, input().split()))
bills = list(map(int, input().split()))
sum_to_masks = {}
for mask in range(1 << m):
    s = 0
    for i in range(m):
        if mask & (1 << i):
            s += bills[i]
    sum_to_masks.setdefault(s, []).append(mask)

print("YES" if f77(0, 0) else "NO")