def can_make_24(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a = nums[i]
            b = nums[j]
            next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
            results = [a + b, a - b, b - a, a * b]
            if abs(b) > 1e-6:
                results.append(a / b)
            if abs(a) > 1e-6:
                results.append(b / a)
            for res in results:
                if can_make_24(next_nums + [res]):
                    return True
    return False

if __name__ == '__main__':
    with open("input.txt") as f:
        T = int(f.readline().strip())
        for _ in range(T):
            data = f.readline().strip().split()
            nums = [float(x) for x in data]
            if can_make_24(nums):
                print("YES")
            else:
                print("NO")
