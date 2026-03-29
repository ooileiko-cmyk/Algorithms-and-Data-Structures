from collections import deque


class Deque:
    def init(self):
        self.data = deque()

    def push_front(self, value):
        self.data.appendleft(value)

    def push_back(self, value):
        self.data.append(value)

    def pop_front(self):
        if not self.data:
            raise IndexError("Deque is empty")
        return self.data.popleft()

    def pop_back(self):
        if not self.data:
            raise IndexError("Deque is empty")
        return self.data.pop()

    def top_front(self):
        if not self.data:
            raise IndexError("Deque is empty")
        return self.data[0]

    def top_back(self):
        if not self.data:
            raise IndexError("Deque is empty")
        return self.data[-1]

    def len(self):
        return len(self.data)