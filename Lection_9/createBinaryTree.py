from BinaryTree import BinaryTree

def createSampleTree():

    """Приклад створення бінарного дерева"""

    # Створимо внутрішні вузли дерева та додаємо до них піддерева
    node8 = BinaryTree(8) # Створення вузла з ключем 8
    node8.setLeft(14) # Додавання лівого піддерева, додаючи листок 14
    node8.setRight(15) # Додавання правого піддерева, додаючи листок 15

    node4 = BinaryTree(4) # Створення вузла з ключем 4
    node4.setLeft(node8) # Додавання лівого піддерева
    node4.setRight(9) # Додавання правого піддерева, додаючи листок 9

    node5 = BinaryTree(5) # Створення вузла з ключем 5

    node5.setLeft(10) # Додавання лівого піддерева, додаючи листок 10
    node5.setRight(11) # Додавання правого піддерева, додаючи листок 11

    # Створюємо корінь дерева та додаємо до нього відповідні вузли

    root = BinaryTree(1)

    root.setLeft(node2) # Додавання лівого піддерева до кореня
    root.setRight(node3) # Додавання правого піддерева до кореня

    return root # Функція повертає корінь створеного дерева