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

        def setitem(self, index, value):
            if index < 0 or index >= self._size:
                raise IndexError("Index out of range")

            current = self.head
            for _ in range(index):
                current = current.next

            current.data = value

            def insert(self, index, value):
                if index < 0 or index > self._size:
                    raise IndexError("Index out of range")

                new_node = Node(value)

                if index == 0:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    current = self.head
                    for _ in range(index - 1):
                        current = current.next

                    new_node.next = current.next
                    current.next = new_node

                self._size += 1

                def index(self, value, start=0, stop=None):
                    if stop is None:
                        stop = self._size

                    current = self.head
                    i = 0

                    while current:
                        if start <= i < stop and current.data == value:
                            return i
                        current = current.next
                        i += 1

                    raise ValueError("Value not found")

    def remove(self, value):
        current = self.head
        prev = None

        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                self._size -= 1
                return

            prev = current
            current = current.next

        raise ValueError("Value not found")