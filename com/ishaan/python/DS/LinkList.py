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
for i in range(1,11):
    new_ll.insert_node_beg(i)
# for i in range(11,21):
#     new_ll.insert_node_end(i)
#new_ll.display_ll()
#print_reverse_ll(new_ll.head)

#rev_ll = LinkedList()
new_ll.display_ll()
ptr = reverse_recursively_ll(new_ll, new_ll.head)
ptr.next = None
new_ll.display_ll()


reverse_ll(new_ll)

new_ll.display_ll()

current = new_ll.head
for i in range(4):
    current = current.next
new_ll2 = LinkedList()
new_ll2.head = current

print('#'*40)
new_ll2.display_ll()
reverse_ll(new_ll2)
new_ll2.display_ll()
print('#'*40)

new_ll.display_ll()









