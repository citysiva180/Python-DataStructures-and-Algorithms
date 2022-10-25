# First create a node class
# Then create a constructor for linked List

# Node class

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:

    # Linked List Constructor

    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):

        # create a temp variable denoting to head.
        # now, on iteration you get to print the values
        # temp.next will traverse to the next value
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_item(self, value):

        new_node = Node(value)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

        else:

            # whats going on here is that... tail and tail.next will direct to the same last node
            # if you see... first we assign the tail.next to the new node which is Node(value)
            # self.tail = new_node is Node(value)

            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return True

    def pop_item(self):

        # For popping list ... you need to do the following

        # Condition 1 the list is not empty and

        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:

            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:

            self.head = new_node
            self.tail = new_node

        else:

            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):

        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):

        # if index is out of range

        if index < 0 or index >= self.length:
            return False

        # if index is at the front or back

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_item(value)

        # Adding an element inside with an index

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1
        return True

    def remove(self, index):

        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop_item()

        pre = self.get(index - 1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None

        self.length -= 1
        return temp

    def reverse_list(self):

        # # The first thing that you would need to do for a reversing a linked list would be
        # # swap the variables  - head and tail

        # temp = self.head

        # self.head = self.tail
        # self.tail = temp

        # after = temp.next
        # before = None

        # # Now iterate through that list from back to front. Just what I thought... although
        # # temp.next should be empty right? temp.next should direct from back to front
        # # before is actually

        # for _ in range(self.length):
        #     after = temp.next
        #     temp.next = before
        #     before = temp
        #     temp = after

        prev = None
        current = self.head

        while (current is not None):
            next = current.next
        current.next = prev

        prev = current
        current = next

        self.head = prev


# Instantiating
linked_list = LinkedList(4)
linked_list.print_list()

# Adding elements
linked_list.append_item(1)
linked_list.append_item(2)
linked_list.append_item(3)
linked_list.append_item(4)
linked_list.append_item(5)
linked_list.append_item(6)
linked_list.append_item(7)
linked_list.append_item(8)
linked_list.append_item(9)

print("after adding elements :  ")

# printing elements

linked_list.print_list()


# pop items in linked list

linked_list.pop_item()
linked_list.pop_item()
linked_list.pop_item()
linked_list.pop_item()
linked_list.pop_item()

print("After removing items ")
linked_list.print_list()


# prepending items in linked list

linked_list.prepend(12)
linked_list.prepend(11)
linked_list.prepend(10)

print("After prepending items ")
linked_list.print_list()


print("getting elements")
getting_elements = linked_list.get(2)
print(getting_elements.value)
getting_elements = linked_list.get(-1)
print(getting_elements)

print("inserting items")
linked_list.insert(2, 456)
linked_list.print_list()

print("after removing")

linked_list.remove(2)
linked_list.print_list()


print("after reversing")
linked_list.reverse_list()
linked_list.print_list()
