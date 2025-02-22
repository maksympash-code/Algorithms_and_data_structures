def max_score(weight, score, num):
    """

    :param weight: поточна вага рюкзака
    :param score: поточна вартість рюкзака
    :param num: номер предмета
    :return:
    """
    global maxScore, W, n #

    if weight == W or num >= n:
        if score > maxScore:
            maxScore = score
        return

    # будуємо наступні варіанти
    max_score(weight, score, num + 1)
    max_score(weight + 1, score + a[m], num + 1)