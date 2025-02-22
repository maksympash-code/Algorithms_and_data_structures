# Побудувати всі можливі n-значні числа, що складаються з цифр 0 та 1

n = int(input())

l = 1 << n - 1
r = 1 << n

for i in range(l, r):
    print(bin(i))

# O(2^n)