class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: [Node | None] = None

class LinkedList:
    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def answer(self) -> str:
        curr = self.head
        res = []
        while curr is not None:
            res.append(str(curr.data))
            curr = curr.next
        return " ".join(res)

    def reverse_list(self, start: [Node | None]) -> [Node | None]:
        prev = None
        curr = start
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def ReorderList(self) -> None:
        if self.head is None or self.head.next is None:
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev is not None:
            prev.next = None

        second = self.reverse_list(slow)
        first = self.head
        dummy = Node(0)
        curr = dummy

        while first is not None or second is not None:
            if first is not None:
                curr.next = first
                curr = curr.next
                first = first.next
            if second is not None:
                curr.next = second
                curr = curr.next
                second = second.next

        self.head = dummy.next

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        self.tail = curr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    linked_list = LinkedList()
    for num in arr:
        linked_list.addToTail(num)
    linked_list.ReorderList()
    print(linked_list.answer())
