from random import randint

class treeNode(object):
    def __init__(self,value):
        self.data = value
        self.right = None
        self.left = None

def BST_insert(root,value):
    new_node = treeNode(value)
    if root is None:
        root = new_node
        return root
    if root.data > value:
        if root.left is None:
            root.left = treeNode(value)
        else:
            BST_insert(root.left,value)
    if root.data < value:
        if root.right is None:
            root.right = treeNode(value)
        else:
            BST_insert(root.right,value)
    return root

def inorder_tree(root):
    if root is None:
        return
    inorder_tree(root.left)
    print(root.data,end=" ")
    inorder_tree(root.right)

def level_order(root):
    if root is None:
        return
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        print(current_node.data,end=" ")
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


my_list = []


counter = 0

while True:
    n = randint(1,100)
    if n not in my_list:
        my_list.append(n)
        counter += 1
        if counter > 30:
            break

#my_list.sort()

#print(my_list)


my_tree = None

for ele in my_list:
    my_tree = BST_insert(my_tree,ele)


inorder_tree(my_tree)
print()
level_order(my_tree)





