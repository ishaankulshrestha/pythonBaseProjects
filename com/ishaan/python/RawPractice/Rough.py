class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

    def insert(self, val):
        # Enter you code here.
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return self.root
        current = self.root
        while current:
            if val < current.info:
                if current.left == None:
                    current.left = new_node
                    return self.root
                else:
                    current = current.left
                    continue
            else:
                if current.right == None:
                    current.right = new_node
                    return self.root
                else:
                    current = current.right
                    continue
        return self.root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
