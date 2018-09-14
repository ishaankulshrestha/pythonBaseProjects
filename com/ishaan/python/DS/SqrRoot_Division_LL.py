class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        return


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert_node_end(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return self.head
        else:
            current = self.head
            while current.next is not None :
                current = current.next
            current.next = new_node
            return self.head

    def insert_node_beg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def display_ll(self):
        current = self.head
        while current is not None:
            print("--> {}".format(current.data),end=" ")
            current = current.next
        print("")


def print_reverse_ll(current):
    if current is None:
        return
    print_reverse_ll(current.next)
    print("--> {}".format(current.data), end=" ")


def reverse_recursively_ll(new_ll, current):
    if current.next is None:
        new_ll.head = current
        return current
    ptr = reverse_recursively_ll(new_ll, current.next)
    ptr.next = current
    return current

def reverse_ll(new_ll):
    prev = None
    current = new_ll.head
    nexts = current.next
    while(current.next is not None):
        current.next = prev
        prev = current
        current = nexts
        nexts = current.next
    current.next = prev
    new_ll.head = current




new_ll = LinkedList()
for i in range(143,0,-1):
    new_ll.insert_node_beg(i)

new_ll.display_ll()

sl_ptr = new_ll.head
fst_ptr = new_ll.head

i = 0
while fst_ptr is not None and fst_ptr.next is not None :
    i = 0
    while  fst_ptr is not None and i < 10:
        fst_ptr = fst_ptr.next
        i += 1
    if fst_ptr is not None :
        sl_ptr = sl_ptr.next
#print(sl_ptr.data)

sl_ptr = new_ll.head
fst_ptr = new_ll.head

i = 0
j = 1
while fst_ptr is not None and fst_ptr.next is not None :
    i = 0

    fst_ptr = new_ll.head
    while fst_ptr is not None and i < j*j:
        fst_ptr = fst_ptr.next
        i += 1
    if fst_ptr is not None:
        sl_ptr = sl_ptr.next
        j += 1

print(sl_ptr.data)

