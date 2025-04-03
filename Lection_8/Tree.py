class Node:
    def __init__(self, key = None):
        self.mKey = key

    def empty(self):
        return self.mKey is None

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey



class Tree(Node):
    def __init__(self, key = None):
        super().__init__(key)
        self.mChildren = []

    def empty(self):
        return super().empty() and len(self.mChildren) == 0

    def addChild(self, child: Tree):
        self.mChildren.append(child)

    def removeChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                self.mChildren.remove(child)
                return True
        return False

    def getChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self.mChildren




def createSampleTree():
    """

    Створювати дерево будемо знизу вгору - спочатку листя,
    потім внутрішні вузли, додаючи до них відповідні піддерева.
    Корінь створимо останнім і додамо до нього відповідні піддерева.
    """

    # Створимо вузли, що є листям дерева

    node7 = Tree(7)
    node9 = Tree(9)
    node10 = Tree(10)
    node11 = Tree(11)
    node12 = Tree(12)
    node13 = Tree(13)
    node14 = Tree(14)
    node15 = Tree(15)
    node8 = Tree(8)
    node8.addChild(node14)
    node8.addChild(node15)

    node4 = Tree(4)
    node4.addChild(node8)
    node4.addChild(node9)

    node5 = Tree(5)
    node5.addChild(node10)
    node5.addChild(node11)

    node2 = Tree(2)
    node2.addChild(node4)
    node2.addChild(node5)

    node6 = Tree(6)
    node6.addChild(node12)
    node6.addChild(node13)

    node3 = Tree(3)
    node3.addChild(node6)
    node3.addChild(node7)

    root = Tree(1)
    root.addChild(node2)
    root.addChild(node3)

    return root

# щоб дістатися до вузла 11
node11 = tree.getChild(2).getChild(5).getChild(11)
