class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1

        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
