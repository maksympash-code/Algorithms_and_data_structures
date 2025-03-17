class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1
        return 'ok'

    def pop(self):
        if self._size == 0:
            return 'error'

        current_top = self.top_node
        self.top_node = current_top.next
        self._size -= 1
        return current_top.item

    def back(self):
        if self._size == 0:
            return 'error'
        return self.top_node.item

    def size(self):
        return self._size

    def clear(self):
        self.top_node = None
        self._size = 0
        return 'ok'

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == 'bye':
                break