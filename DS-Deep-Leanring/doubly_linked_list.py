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
            self.tail.next = new_node  # type: ignore
            new_node.prev = self.tail  # type: ignore
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
            self.tail = self.tail.prev  # type: ignore
            self.tail.next = None  # type: ignore
            temp.prev = None  # type: ignore

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # type: ignore
            self.head.prev = new_node  # type: ignore
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # if you have no items in the list
        if self.length == 0:
            return None
        temp = self.head
        # if you have only 1 item in the list
        if self.length == 1:
            self.head = None
            self.head = None
        else:
            self.head = self.head.next  # type: ignore
            self.head.prev = None  # type: ignore
            temp.next = None  # type: ignore
        self.length -= 1
        return temp

    def get(self, index):
        # if the index is less than 0 or greater / equal to self.length
        # Then you need to return nothing
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next  # type: ignore
            return temp
        else:
            temp = self.tail
            # reverse loop
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  # type: ignore
            return temp

    def set(self, index, value):
        # reuse the code from get... gentle and smart
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.length
        if index == self.length:
            return self.append(value)  # type: ignore

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next  # type: ignore

        new_node.prev = before  # type: ignore
        new_node.next = after
        before.next = new_node  # type: ignore
        after.prev = new_node  # type: ignore
        
        self.length +=1 
        return True

    def remove_item(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()  # type: ignore

        temp = self.get(index)
        temp.next.prev = temp.prev  # type: ignore
        temp.prev.next = temp.next  # type: ignore
        temp.next = None  # type: ignore
        temp.prev = None  # type: ignore

        self.length -= 1
        return temp


ddl_1 = DoublyLinkedList(0)

# Adding elements in the ddl

print("Adding Elements in a doubly linked list")

ddl_1.append_item(1)
ddl_1.append_item(2)
ddl_1.append_item(3)
ddl_1.append_item(4)
ddl_1.append_item(5)
ddl_1.append_item(6)
ddl_1.append_item(7)
ddl_1.append_item(8)
ddl_1.append_item(9)
ddl_1.append_item(10)

# Printing the entire list

ddl_1.print_list()

# Poping an item in the list

print("Popping an Item - Removes element from last ")

ddl_1.pop_item()
ddl_1.print_list()

# Prepending an Item
print("Prepending an Item - Adds element at first")

ddl_1.prepend(100)
ddl_1.print_list()

# Pop first
print("Pop-First - Removing an element from the front")

ddl_1.pop_first()
ddl_1.print_list()

# Set

print("Set - Setting an element at a certain index")

ddl_1.set(3, 100)
ddl_1.print_list()

# Get

print("Get - Reading an element at certain index")

new_num = ddl_1.get(3)
print(new_num.value)  # type: ignore

# Insert

print("Insert an element in the middle")
ddl_1.insert_value(5, 2000)
ddl_1.print_list()

# Remove

print("Removing an item")
ddl_1.remove_item(4)
ddl_1.print_list()
