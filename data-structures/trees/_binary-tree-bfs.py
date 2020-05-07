from collections import deque

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


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        qu = Queue()
        visit_order = list()
        node = self.get_root()
        qu.enq((node, level))

        while len(qu) > 0:
            node, level = qu.deq()
            if node == None:
                visit_order.append(("empty", level))
                continue

            visit_order.append((node, level))
            if node.has_left_child():
                qu.enq((node.get_left_child(), level + 1))
            else:
                qu.enq((None, level + 1))

            if node.has_right_child():
                qu.enq((node.get_right_child(), level + 1))
            else:
                qu.enq((None, level + 1))

        s = "Tree\n"
        prev_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == prev_level:
                s += " | " + str(node)
                prev_level = level
            else:
                s += "\n" + str(node)
                prev_level = level

        return s


def bfs(tree):
    qu = Queue()
    visit_order = list()
    node = tree.get_root()
    qu.enq(node)

    while len(qu) > 0:
        node = qu.deq()
        visit_order.append(node)
        if node.has_left_child():
            qu.enq(node.get_left_child())
        if node.has_right_child():
            qu.enq(node.get_right_child())

    return visit_order


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
# print(tree)

print(bfs(tree)) # [Node(apple), Node(banana), Node(cherry), Node(dates)]