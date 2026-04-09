class Queue:
    def init(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data.pop(0)

    def top(self):
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data[0]

    def len(self):
        return len(self.data)