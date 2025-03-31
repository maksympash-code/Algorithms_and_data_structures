class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = None          # Посилання на перший вузол
current_node = None  # Посилання на «поточний» вузол

def init():
    """
    Викликається один раз на початку виконання програми.
    Очищає список і скидає поточний елемент.
    """
    global head, current_node
    head = None
    current_node = None

def empty():
    """
    Перевіряє, чи список порожній.
    :return: True, якщо список не містить жодного елемента
    """
    return head is None

def reset():
    """
    Робить перший елемент списку поточним.
    Гарантується, що не буде викликана, якщо список порожній.
    """
    global current_node
    current_node = head

def next():
    """
    Перейти до наступного елемента.
    Робить елемент, що йде за поточним, новим поточним.
    Якщо поточний елемент є останнім у списку, викликає StopIteration.
    """
    global current_node
    if current_node is None or current_node.next is None:
        raise StopIteration("Поточний елемент є останнім у списку.")
    current_node = current_node.next

def current():
    """
    Повертає значення (навантаження) поточного елементу.
    Гарантується, що не буде викликатися, якщо список порожній.
    """
    global current_node
    return None if current_node is None else current_node.value

def insert_after(item):
    """
    Вставляє новий елемент у список після поточного.
    Якщо список порожній, створюється новий елемент, який стає і head, і поточним.
    Якщо список не порожній, новий елемент вставляється після current_node.
    """
    global head, current_node
    new_node = Node(item)
    if empty():
        head = new_node
        current_node = new_node
    else:
        new_node.next = current_node.next
        current_node.next = new_node

def insert_before(item):
    """
    Вставляє новий елемент у список перед поточним.
    Якщо список порожній, створюється перший вузол (head) і він же стає поточним.
    Якщо поточний - перший елемент, новий вузол стає новим head.
    Інакше шукаємо «попередній» (prev) вузол, щоб уставити new_node між ним і current_node.
    Поточний елемент не змінюється.
    """
    global head, current_node
    new_node = Node(item)
    if empty():
        head = new_node
        current_node = new_node
        return

    if current_node == head:
        new_node.next = head
        head = new_node
        return

    prev = head
    while prev.next and prev.next != current_node:
        prev = prev.next
    new_node.next = current_node
    prev.next = new_node

def delete():
    """
    Видаляє поточний елемент.
    Поточним стає наступний елемент, якщо він існує.
    Якщо видаляється останній вузол, поточним стає попередній вузол.
    Гарантується, що виклик не відбувається, якщо список порожній.
    """
    global head, current_node

    if empty():
        return

    if current_node == head and current_node.next is None:
        head = None
        current_node = None
        return

    if current_node == head:
        head = head.next
        current_node = head
        return

    prev = head
    while prev.next and prev.next != current_node:
        prev = prev.next

    nxt = current_node.next
    prev.next = nxt


    if nxt is not None:
        current_node = nxt
    else:
        current_node = prev



def damp():
    """
    Повертає список усіх елементів (у порядку з head до кінця).
    """
    global head
    result = []
    node = head

    while node is not None:
        result.append(node.value)
        node = node.next
    return result
