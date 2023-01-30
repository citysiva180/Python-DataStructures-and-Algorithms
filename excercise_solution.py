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
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore
            self.tail = new_node
        self.length += 1
        return True

    ### WRITE POP METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################

    def pop(self):
        
        if self.length == 0:
            return None 
        
        temp    = self.head
        pre     = self.head
        
        while(temp.next): # type: ignore
            pre = temp
            temp = temp.next # type: ignore
        self.tail  = pre 
        self.tail.next = None # type: ignore
        self.length -= 1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
        return temp


# DO NOT EDIT CODE BELOW THIS LINE
my_linked_list = LinkedList(1)
my_linked_list.append(2)
# (2) Items - Returns 2 Node
print(my_linked_list.pop().value) # type: ignore
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value) # type: ignore
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
