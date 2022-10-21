# First create a node class
# Then create a constructor for linked List

# Node class

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

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
    
    def pop_item(self, value):
        
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
        
        
            
    
