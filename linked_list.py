class Node:
    def init(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def init(self, iterable=None):
        self.head = None
        self._size = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def len(self):
        return self._size

    def repr(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self._size += 1

        def getitem(self, index):
            if index < 0 or index >= self._size:
                raise IndexError("Index out of range")

            current = self.head
            for _ in range(index):
                current = current.next

            return current.data
