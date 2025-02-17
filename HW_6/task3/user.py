
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

size = 100003
DELETED = ("__DELETED__", "__DELETED__")

def custom_hash(author, title, attempt=0):
    return (hash(author + "#" + title) + attempt) % size



def init():
    """ Викликається 1 раз на початку виконання програми. """
    global hash_table
    hash_table = [None for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    attempt = 0
    while attempt < size:
        index = custom_hash(author, title, attempt)
        if hash_table[index] is None or hash_table[index] == DELETED:
            hash_table[index] = (author, title)
            return
        attempt += 1


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    attempt = 0
    while attempt < size:
        index = custom_hash(author, title, attempt)
        if hash_table[index] is None:
            return False
        if hash_table[index] == (author, title):
            return True
        attempt += 1
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    attempt = 0
    while attempt < size:
        index = custom_hash(author, title, attempt)
        if hash_table[index] is None:
            return
        if hash_table[index] == (author, title):
            hash_table[index] = DELETED
            return
        attempt += 1

def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    books = []

    for entry in hash_table:
        if entry is not None and entry != DELETED and entry[0] == author:
            books.append(entry[1])

    return sorted(books) if books else []

