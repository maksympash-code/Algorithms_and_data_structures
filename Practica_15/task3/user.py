#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

head: [Node | None] = None
tail: [Node | None] = None # Кінець списку
current_node: Node | None = None

def init():
    global head, tail, current_node
    head = None
    tail = None
    current_node = None


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return head is None


def set_first():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global current_node
    current_node = head


def set_last():
    """ Робить останній елемент списку, поточним

    Переставляє поточний елемент на останній елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global current_node
    current_node = tail


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    global current_node
    if current_node is None or current_node.next is None:
        raise StopIteration
    current_node = current_node.next


def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    global current_node
    if current_node is None or current_node.prev is None:
        raise StopIteration
    current_node = current_node.prev


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return None if current_node is None else current_node.value


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    global head, tail, current_node
    new_node = Node(item)

    if empty():
        head = new_node
        tail = new_node
        current_node = new_node
    else:
        new_node.prev = current_node
        new_node.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = new_node
        else:
            tail = new_node
        current_node.next = new_node




def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    pass


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    pass
