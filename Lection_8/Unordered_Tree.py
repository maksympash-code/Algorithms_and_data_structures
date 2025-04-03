class Node:
    def __init__(self, key = None):
        self.mKey = key


    def empty(self):
        return self.mKey is None

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey



class UnorderedTree(Node):
    def __init__(self, key = None):
        super().__init__(key)
        self.mChildren = {}

    def empty(self):
        return super().empty() and len(self.mChildren) == 0

    def addChild(self, child: UnorderedTree):
        self.mChildren[child.key()] = child

    def removeChild(self, key):
        for child in self.mChildren.values():
            if child.key() == key:
                self.mChildren.pop(child.key())
                return True
        return False

    def getChild(self, key):
        for child in self.mChildren.values():
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return list(self.mChildren.values())