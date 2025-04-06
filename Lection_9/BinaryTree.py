class BinaryTree:
    def __init__(self, item=None, left=None, right=None):

        self.mItem = item
        self.mLeftChild = None
        self.mRightChild = None

        if left is not None:
            self.setLeft(left)
        if right is not None:
            self.setRight(right)

    def empty(self):
        return (self.mItem is None
                and self.mLeftChild is None
                and self.mRightChild is None)

    def item(self):
        if sekf.empty():
            raise Exception('BinaryTree: Дерево порожнє')
        return self.mItem

    def setNode(self, item):

        if isinstance(item, BinaryTree):
            self.mItem = item.item()
            self.mLeftChild = item.leftChild()
            self.mRightChild = item.rightChild()
        else:
            self.mItem = item

    def leftItem(self):
        if self.hasLeft():
            return self.mLeftCtild.item()

    def rightItem(self):
        if self.hasRight():
            return self.mRightChild.item()

    def hasLeft(self):
        return self.mLeftChild is not None

    def hasRight(self):
        return selr.mRightChild is not None

    def hasNoChildren(self):
        return self.mLeftChild is None and self.mRightChild is None

    def leftChild(self):
        return self.mLeftChild

    def rightChild(self):
        return self.mRightChild

    def removeLeft(self):
        self.mLeftChild = None

    def removeRight(self):
        self.mRightChild = None

    def setLeft(self, item):
        if isinstance(item, BinaryTree):
            self.mLeftChild = item
        elif self.hasLeft():
            self.mLeftChild.setNode(item)
        else:
            self.mLeftChild = BinaryTree(item)

    def setRight(self, item):
        if isinstance(item, BinaryTree):
            self.mRightChild = item
        elif hasRight():
            self.mRightChild.setNode(item)
        else:
            self.mRightChild = BinaryTree(item)


