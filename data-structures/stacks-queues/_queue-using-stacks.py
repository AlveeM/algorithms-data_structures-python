class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.main_stack = Stack()
        self.dequeue_stack = Stack()

    def size(self):
        return self.main_stack.size() + self.dequeue_stack.size()

    def enqueue(self, item):
        self.main_stack.push(item)

    def dequeue(self):
        if not self.dequeue_stack.items:
            while self.main_stack:
                self.dequeue_stack.push(self.main_stack.pop())

        return self.dequeue_stack.pop()
