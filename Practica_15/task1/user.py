class Node:
    def __init__(self, value):
        self.value = value
        self.next: [Node | None] = None

# Глобальні змінні для зберігання початку списку та поточного елемента
head: [Node | None] = None
current_node: [Node | None] = None

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
    Гарантується, що не буде викликана, якщо список порожній.
    """
    global current_node
    if current_node is None:
        return None
    return current_node.value

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
        return

    new_node.next = current_node.next
    current_node.next = new_node
