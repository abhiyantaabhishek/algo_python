class BinaryTree:
    def __init__(self):

        self.left = None
        self.right = None
        self.data = None


def node(data):
    bTree = BinaryTree()
    bTree.left = None
    bTree.right = None
    bTree.data = data
    return bTree


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)


def preorder_traversal(root: BinaryTree):
    if root == None:
        return
    else:
        preorder_traversal(root.left)
        print(root.data)
        preorder_traversal(root.right)


preorder_traversal(root)
#%%
def fun(arr, a):
    arr[0] = 10
    a = 6


def fun2():
    arr = [1, 2, 3]
    a = 0
    fun(arr, a)
    print(arr, a)


fun2()


#%%
