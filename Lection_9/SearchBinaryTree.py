from BinaryTree import BinaryTree
# Реалізовується на основі простого Бінарного Дерева
class SearchBinaryTree(BinaryTree):
    def __init__(self, key):
        super().__init__(key)  # Передаємо key батьківському конструктору
        self.mKey = key        # Якщо потрібно зберігати ключ у полі mKey



    def search(self, key):

        """ Метод, що реалізує пошук елемента item у бінарному дереві
        Не рекурсивна реалізація
        :param key: Шуканий елемент
        :return: Вузол з ключем key якщо такий елемент міститься у дереві
        та None - якщо елемент не знайдений. """

        node = self
        while node is not None:
            if key == node.mKey:
                return node
            elif key < node.mKey:
                node = node.mLeftChild
            else:
                node = node.mRightChild

        return None

    def rSearch(self, key):

        """ Метод, що реалізує пошук елемента item у бінарному дереві
        Рекурсивна реалізація
        :param key: Шуканий елемент
        :return: Вузол з ключем key якщо такий елемент міститься у дереві

        та None - якщо елемент не знайдений. """

        node = self

        if key == node.mKey:
            return node
        elif key < node.mKey:
            if node.hasLeft():
                return node.mLeftChild.rSearch(key)
        else:
            if node.hasRight():
                return node.mRightChild.rSearch(key)
        return None


    def insert(self, key):

        """ Метод, що реалізує вставку елемента у бінарне дерево
        Не рекурсивна реалізація
        :param key: ключ, що необхідно вставити """

        if self.empty():
            self.setNode(key)
        else:
            node = self
            while True:
                if key == node.mKey:
                    break
                elif key < node.mKey:
                    if node.hasLeft():
                        node = node.mLeftChild
                    else:
                        node.setLeft(key)
                        break
                elif key > node.mKey:
                    if node.hasRight():
                        node = node.mRightChild
                    else:
                        node.setRight(key)
                        break

    def rInsert(self, key):

        """ Метод, що реалізує вставку елемента у бінарне дерево
        Рекурсивна реалізація
        :param key: ключ, що необхідно вставити """

        if self.empty():
            self.setNode(key)
        else:
            node = self

            if key < node.mKey:
                if node.hasLeft():
                    node.mLeftChild.rInsert(key)
                else:
                    node.setLeft(key)

            elif key > node.mKey:
                if node.hasRight():
                    node.mRightChild.rInsert(key)
                else:
                    node.setRight(key)