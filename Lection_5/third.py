# За заданим натуральним числом n виведемо усі перестановки з цілих чисел від 1 до n
# n = 1, 2, 3


def sequences(lst: list, k, n):
    """
    :param lst: підсписок перестановок
    :param k: елемент для вставки
    :param n: найбільший елемент послідовності
    :return:
    """
    if k > n: # Якщо всі елементи вже вичерпано
        print(*lst)
        return

    # Вставляємо елемент k у всі можливі позиції списку
    # отриманого на попередніх ітераціях
    for pos in range(k):
        lst_next = lst[:]               # Копіюємо список
        lst_next.insert(pos, k)         # вставляємо елемент
        sequences(lst_next, k + 1, n)   # рекурсивне додавання наступного елемента

n = int(input())
lst = []
sequences(lst, 1, n)