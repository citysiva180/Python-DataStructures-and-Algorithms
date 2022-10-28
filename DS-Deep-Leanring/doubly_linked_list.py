# This code deals with double linked list

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # Creating a constructor

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Printing list

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Appending Items in a doubly Linked List
    def append_item(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # Popping in Doubly Linked List

    def pop_item(self):

        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True


ddl_1 = DoublyLinkedList(7)
ddl_1.print_list()
ddl_1.append_item(5)
ddl_1.print_list()
ddl_1.pop_item()
ddl_1.print_list()

# if self.length == 0:
#     return None
# temp  = self.tail
# self.tail = self.tail.prev
# self.tail.next  = None
# temp.prev = None
# self.length -= 1
# if self.length == 0:
#     self.head = None
#     self.head = None
print("prepend")
ddl_1.prepend(3)
ddl_1.print_list()
