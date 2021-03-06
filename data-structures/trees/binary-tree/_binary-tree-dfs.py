class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

#           apple
#          /    \
#      banana   cherry
#       /
#   dates

def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            visit_order.append(node.value)
            traverse(node.get_left_child())
            traverse(node.get_right_child())

    traverse(root)
    return visit_order

print(pre_order(tree)) # ['apple', 'banana', 'dates', 'cherry']

def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node.value)
            traverse(node.get_right_child())

    traverse(root)
    return visit_order

print(in_order(tree)) # ['dates', 'banana', 'apple', 'cherry']

def post_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visit_order.append(node.value)

    traverse(root)
    return visit_order

print(post_order(tree)) # ['dates', 'banana', 'cherry', 'apple']