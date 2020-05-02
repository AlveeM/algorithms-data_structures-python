class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        while node.next:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("value not found")

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("value not found")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        node = self.head

        if node is None:
            return node

        self.head = self.head.next
        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        # if empty list: update head
        if self.head is None:
            self.head = Node(value)
            return

        # if pos 0: prepend
        if pos == 0:
            self.prepend(value)
            return

        idx = 0
        node = self.head
        while node.next and idx <= pos:
            # if idx === pos - 1: insert node
            if idx == (pos - 1):
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            idx += 1
            node = node.next

        # if pos > size
        self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next

        return count

    def to_list(self):
        output_list = []

        current_node = self.head
        while current_node:
            output_list.append(current_node.value)
            current_node = current_node.next

        return output_list

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"