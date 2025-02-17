
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
from fontTools.mtiLib import bucketizeRules

size = 100003

def _hash(author, title):
    return hash(author + "#" + title) % size

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global hash_table
    hash_table = [[] for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global hash_table
    index = _hash(author, title)
    for entry in hash_table[index]:
        if entry == (author, title):
            return
    hash_table[index].append((author, title))


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global hash_table
    index = _hash(author, title)
    for entry in hash_table[index]:
        if entry == (author, title):
            return True
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global hash_table
    index = _hash(author, title)
    bucket = hash_table[index]
    for i, entry in enumerate(bucket):
        if entry == (author, title):
            del bucket[i]
            return


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global hash_table
    books = []
    for bucket in hash_table:
        for entry in bucket:
            if entry[0] == author:
                books.append(entry[1])
    return sorted(books) if books else []

