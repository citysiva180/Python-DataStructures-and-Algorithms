class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node  # type: ignore
            self.last = new_node
    
    def dequeue(self):
        
        if self.length == 0:
            return None
        
        temp = self.first 
        
        if self.length == 1:
            self.first = None 
            self.last = None
        else: 
            self.first = self.first.next #type: ignore
            temp.next = None #type: ignore
        self.length -= 1
        return temp


my_queue = Queue(9)
my_queue.print_queue()
my_queue.enqueue(10)
my_queue.print_queue()
