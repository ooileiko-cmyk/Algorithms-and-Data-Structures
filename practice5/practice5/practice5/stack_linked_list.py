class Node:
    def init(self, data):
        self.data = data
        self.next = None


class Stack:
    def init(self):
        self.top_node = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1

    def pop(self):
        if not self.top_node:
            raise IndexError("Stack is empty")

        value = self.top_node.data
        self.top_node = self.top_node.next
        self._size -= 1
        return value

    def top(self):
        if not self.top_node:
            raise IndexError("Stack is empty")
        return self.top_node.data

    def len(self):
        return self._size