from random import randint

class treeNode(object):
    def __init__(self,value):
        self.data = value
        self.right = None
        self.left = None

def BST_insert_list(my_list,start,end):
    if start > end or start >= len(my_list):
        return
    if start == end:
        return treeNode(my_list[start])
    root = treeNode(my_list[(start+end)//2])
    root.left = BST_insert_list(my_list,start,(start+end)//2)
    #print(" {} {} {}".format(start,(start+end)//2,end))
    root.right = BST_insert_list(my_list,((start+end)//2)+1,end)
    return root

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
    queue = [[root,0,1]]
    prev = 0
    while queue:
        [current_node,level,position] = queue.pop(0)
        level = level + 1
        if prev < level:
            prev = level
            print()
            print(" "*position)
            position = 1
            spacing = 100

        print("{}".format(current_node.data,position,level),end=" ")
        spacing = 1
        position += 1
        if current_node.left:
            queue.append([current_node.left,level,position])
        position += 1
        if current_node.right:
            queue.append([current_node.right,level,position])


## Main programme

my_list = []


counter = 0

while True:
    n = randint(1,100)
    if n not in my_list:
        my_list.append(n)
        counter += 1
        if counter > 32:
            break

my_list.sort()

print(my_list)


my_tree = None

for ele in my_list:
    my_tree = BST_insert(my_tree,ele)


inorder_tree(my_tree)
print()
level_order(my_tree)

my_tree2 = None

my_tree2 = BST_insert_list(my_list,0,len(my_list))

level_order(my_tree2)








