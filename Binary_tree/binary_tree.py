from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_order(root: Node):
    if root != None:
        print(root.value, end=" ")
        pre_order(root.left)
        pre_order(root.right)


def pre_order_non_reursive_1(root: Node):
    stack = deque()
    stack.append(root)
    while len(stack) != 0:
        temp_node = stack.pop()

        print(temp_node.value, end=" ")
        if temp_node.right != None:
            stack.append(temp_node.right)
        if temp_node.left != None:
            stack.append(temp_node.left)


def pre_order_non_reursive_2(root: Node):
    stack = deque()
    while root != None or len(stack) != 0:
        while root != None:
            print(root.value, end=" ")
            stack.append(root.right)
            root = root.left
        if len(stack) != 0:
            root = stack.pop()


def in_order(root: Node):
    if root != None:
        in_order(root.left)
        print(root.value, end=" ")
        in_order(root.right)


def in_order_non_reursive(root: Node):
    stack = deque()
    while root != None or len(stack) != 0:
        while root != None:
            stack.append(root)
            root = root.left
        if len(stack) != 0:
            root = stack.pop()
            print(root.value, end=" ")
            root = root.right


def post_order(root: Node):
    if root != None:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end=" ")


def post_order_non_reursive(root: Node):
    stack = []  # deque()
    while root != None or len(stack) != 0:
        while root != None:
            if root.right != None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.right != None and len(stack) > 0 and root.right == stack[-1]:
            stack.pop()
            stack.append(root)
            root = root.right
        # elif root.right == None:
        else:
            print(root.value, end=" ")
            root = None


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(" " * 4 * level + "->", node.value)
        printTree(node.left, level + 1)


def get_height(root: Node):
    if root == None:
        return 0
    else:
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        return max(left_height, right_height) + 1


def level_order_traversal(root: Node):
    for i in range(1, get_height(root) + 1):
        curr_level(root, i)


def curr_level(root: Node, level):
    if level == 1:
        print(root.value, end=" ")
        return
    else:
        curr_level(root.left, level - 1)
        curr_level(root.right, level - 1)


def level_order_traversal_non_reursive(root: Node):
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        root = queue.popleft()
        print(root.value, end=" ")
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)


btree = Node(0)
btree.right = Node(4)
btree.left = Node(2)
btree.left.right = Node(5)
btree.left.left = Node(6)
btree.right.left = Node(12)
btree.right.right = Node(10)

printTree(btree)
print("\npre_order:")
pre_order(btree)
print("\npre_order_non_reursive_2:")
pre_order_non_reursive_2(btree)
print("\nin_order:")
in_order(btree)
print("\nin_order_non_reursive:")
in_order_non_reursive(btree)
print("\npost_order:")
post_order(btree)
print("\npost_order_non_reursive:")
post_order_non_reursive(btree)
print("\nlevel_order_traversal:")
level_order_traversal(btree)
print("\nlevel_order_traversal_non_reursive:")
level_order_traversal_non_reursive(btree)

