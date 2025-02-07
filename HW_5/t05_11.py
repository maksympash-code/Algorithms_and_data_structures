def solve():
    R, L, B = map(int, input().split())  # Кількість полів, межа координат, бюджет
    x = [int(input()) for _ in range(R)]  # Зчитуємо координати полів

    # Обчислюємо префіксні суми для швидкого обчислення вартості транспортування
    prefix = [0] * (R + 1)
    for i in range(R):
        prefix[i + 1] = prefix[i] + x[i]

    # Функція, що перевіряє, чи можна перевезти хоча б k вантажівок,
    # тобто знайти суміжний блок розміром k з сумарною вартістю ≤ B.
    def can_deliver(k):
        if k == 0:
            return True
        # Перебираємо усі можливі блоки розміром k
        for i in range(0, R - k + 1):
            # Індекс медіани у вибраному блоці
            m = i + (k - 1) // 2
            med = x[m]
            left_count = m - i
            right_count = (i + k - 1) - m
            cost_left = med * left_count - (prefix[m] - prefix[i])
            cost_right = (prefix[i + k] - prefix[m + 1]) - med * right_count
            total_cost = cost_left + cost_right
            if total_cost <= B:
                return True
        return False

    # Бінарний пошук для знаходження максимальної кількості вантажівок
    l = 0
    r = R + 1
    while r - l > 1:
        m = (l + r) // 2
        if can_deliver(m):
            l = m
        else:
            r = m

    # Виводимо відповідь
    print(l)

if __name__ == '__main__':
    solve()
