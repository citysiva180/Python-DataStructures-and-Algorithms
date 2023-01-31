class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top  # type: ignore
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next # type: ignore
        temp.next = None  # type: ignore
        self.height -= 1
        return temp
    
    


my_stack = Stack(4)
# my_stack.print_stack()
my_stack.push(12)
my_stack.push(14)
my_stack.push(15)
my_stack.print_stack()
my_stack.pop()
print("after popping")
my_stack.print_stack()
