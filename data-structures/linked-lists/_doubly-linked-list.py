class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:
            # set head to new node
            self.head = new_node
            # set tail to head node
            self.tail = self.head
            return

        # append new node to the end
        self.tail.next = new_node
        # point new node's prev attribute to old tail node
        self.tail.next.prev = self.tail
        # update tail attribute with new node
        self.tail = self.tail.next
        return


# Test your class here

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.prev