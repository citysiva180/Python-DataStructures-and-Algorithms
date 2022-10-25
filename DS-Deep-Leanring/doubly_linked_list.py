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
            
    # Appending list 
    
    def append_item(self, value):
        
        if self.head is None: 
            self.head = new_node
            self.tail = new_node 
    
    
            
            


ddl_1 = DoublyLinkedList(7)
ddl_1.print_list()
