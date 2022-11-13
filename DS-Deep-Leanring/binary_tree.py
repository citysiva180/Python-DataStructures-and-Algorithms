class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        # Create an instance of the node

        new_node = Node(value)

        # If there are no values in the tree.
        # then you create a new node and assign the value to the node
        # and then you add that value to that tree. Now the tree length will be 1

        if self.root is None:
            self.root = new_node
            return True

        # Now if there are elements in the tree.
        # then you need to take efforts to insert the value into the tree.
        # For this... you would need to check..what value is present.

        temp = self.root

        while (True):

            # Now if the value is same as the node value.
            # it will not be inserted!

            if new_node.value == temp.value:
                return False

            # If the value is less than node value
            # then you need to assign this value to the left of temp.
            # but only if there are no value is present in the left you go ahead.

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node  # type: ignore
                    return True
               
                # A very important note would be that... if there is a value in the left of the system... then 
                # we got to temp = temp.left which is again an iteration to the next element. This will go until the element comes to None     
                
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node  # type: ignore
                    return True


my_tree = Binary_Search_Tree()

print(my_tree.root)
