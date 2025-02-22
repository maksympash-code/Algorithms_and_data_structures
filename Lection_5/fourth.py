# За заданим натуральним числом n виведемо усі перестановки з цілих чисел від 1 до n у лексикографічному порядку
# n = 1, 2, 3

def sequences(lst: list, n):
    """
    :param lst: підсписок перестановок
    :param n:   найбільший елемент
    :return:
    """

    k = len(lst)

    if k == n:
        print(*lst)
        return

    for i in range(1, n + 1):
        if i not in lst:
            lst_next = lst[:]
            lst_next.append(i)
            sequences(lst_next, n)

n = int(input())
lst = []
sequences(lst, n)