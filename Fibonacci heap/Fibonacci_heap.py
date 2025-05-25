


class FibNode:
    def __init__(self, key, value=None):
        self.key = key            # пріоритет
        self.value = value        # довільне навантаження
        self.degree = 0           # число дітей
        self.mark = False         # прапорець для каскадних відтинань
        self.parent = None
        self.child = None
        # брати у кільці (коло-бісписок)
        self.left = self
        self.right = self

class FibHeap:
    def __init__(self):
        self.min = None           # вказівник на вузол із мінімальним ключем
        self.n = 0                # загальна кількість вузлів

    def insert(self, node: FibNode):
        """Вставка нового вузла — Θ(1) амортизовано."""
        node.degree = 0
        node.parent = node.child = None
        node.mark = FalseІ
        if self.min is None:
            self.min = node
        else:
            # вставляємо node у кореневе кільце праворуч від min
            node.left = self.min
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node
            if node.key < self.min.key:
                self.min = node
        self.n += 1

    def find_min(self):
        """Повернути вузол із мінімальним ключем за O(1)."""
        return self.min

    def union(self, other: 'FibHeap'):
        """Об’єднати дві Sкупи за Θ(1) амортизовано."""
        H = FibHeap()
        # якщо одна з куп порожня
        if not self.min:
            return other
        if not other.min:
            return self
        # зʼєднати два кореневі кільця
        a = self.min.right
        b = other.min.left
        self.min.right = other.min
        other.min.left = self.min
        a.left = b
        b.right = a
        # мінімум — той, у кого менший ключ
        H.min = self.min if self.min.key < other.min.key else other.min
        H.n = self.n + other.n
        return H

    def extract_min(self):
        """Видобути мінімальний вузол — O(log n) амортизовано."""
        z = self.min
        if z is not None:
            # 1) Додаємо всіх дітей z у кореневий список
            if z.child:
                children = [x for x in self._iterate(z.child)]
                for x in children:
                    x.parent = Noneі
                    # вирізати x з кільця дітей
                    x.left.right = x.right
                    x.right.left = x.left
                    # додати x у корені
                    x.left = self.min
                    x.right = self.min.right
                    self.min.right.left = x
                    self.min.right = x
            # 2) Видалити z з кореневого кільця
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()
            self.n -= 1
        return z

    def decrease_key(self, x: FibNode, new_key):
        """Зменшити ключ вузла x — Θ(1) амортизовано."""
        if new_key > x.key:
            raise ValueError("Новий ключ більший за старий!")
        x.key = new_key
        y = x.parent
        if y and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def _cut(self, x: FibNode, y: FibNode):
        """Видалити x із списку дітей y і зробити його коренем."""
        # якщо x — єдиний дитина
        if y.child == x:
            y.child = x.right if x.right != x else None
        # вирізати x з кільця
        x.left.right = x.right
        x.right.left = x.left
        y.degree -= 1
        # додати x у кореневий список
        x.parent = None
        x.left = self.min
        x.right = self.min.right
        self.min.right.left = x
        self.min.right = x
        x.mark = False

    def _cascading_cut(self, y: FibNode):
        """Каскадне відтинання вершини y."""
        z = y.parent
        if z:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _consolidate(self):
        """Обʼєднати корені однакового степеня — O(log n)."""
        import math
        D = int(math.log(self.n, 1.618)) + 2
        A = [None] * (D+1)
        # для кожного кореня
        for w in list(self._iterate(self.min)):
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        # відновити кореневий список і мінімум
        self.min = None
        for node in A:
            if node:
                node.left = node.right = node
                if not self.min:
                    self.min = node
                else:
                    node.left = self.min
                    node.right = self.min.right
                    self.min.right.left = node
                    self.min.right = node
                    if node.key < self.min.key:
                        self.min = node

    def _link(self, y: FibNode, x: FibNode):
        """Зробити y дитиною x (y.key ≥ x.key)."""
        # вирізати y з коренів
        y.left.right = y.right
        y.right.left = y.left
        # приєднати y як дитину x
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y.right = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y
        x.degree += 1
        y.mark = False

    def _iterate(self, start: FibNode):
        """Ітератор по циклічному кільцю, починаючи з start."""
        node = start
        while True:
            yield node
            node = node.right
            if node == start:
                break

# -----------------------
# Приклад використання:
if __name__ == "__main__":
    H = FibHeap()
    # вставляємо ключі 3, 7, 1, 5
    for k in [3,7,1,5]:
        H.insert(FibNode(k))
    print("Min =", H.find_min().key)  # 1

    # зменшуємо ключ 7→0
    node7 = next(n for n in H._iterate(H.min) if n.key == 7)
    H.decrease_key(node7, 0)
    print("New Min =", H.find_min().key)  # 0

    # витягуємо по одному мін
    while H.n:
        m = H.extract_min()
        print("Extracted", m.key)
