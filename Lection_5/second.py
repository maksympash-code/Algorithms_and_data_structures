# Програма, що визначає кількості тризначних натуральних чисел, сума цифр яких = n (n >= 1)

n = int(input())
counter = 0

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if i + j + k == n:
                counter += 1

print(counter)