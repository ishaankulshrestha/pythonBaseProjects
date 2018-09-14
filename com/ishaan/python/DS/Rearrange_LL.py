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



new_ll = LinkedList()
for i in range (1,11,1):
    new_ll.insert_node_end(i)

new_ll.display_ll()

slowptr = new_ll.head
fastpts = new_ll.head

while fastpts is not None and fastpts.next is not None:
    for i in range(2):
        if fastpts is None:
            break
        fastpts = fastpts.next
    slowptr

