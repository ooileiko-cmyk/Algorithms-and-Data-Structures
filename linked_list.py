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