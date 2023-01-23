# Trees

# A tree is basically a linked list. A LL is actually a tree that does not fork..

# A Tree actually has a node that points to 2 notes. This is known as binary tree

# FULL TREE

# A Full tree is a tree where the nodes points to zero nodes or 2 nodes

# PERFECT TREE

# A Perfect tree has all of its level filled up.

# COMPLETE TREE

# A Complete tree has all of its node pointing to 2 nodes.

# Child nodes and Parent nodes

# Child nodes are the 2 nodes below
# Parent node is a node which is pointing to 2 nodes
# The end node after which no nodes come up are the nodes known as leaf

# Binary Tree and Binary Search Tree...


# In a Binary Tree we keep the larger number at right and lower number at left
# Suppose a number is greater than the parent node at level 1 but lower than parent node at level 2 then it goes to left of parent node level 2

# Binary search tree - BIG O
# 2^1 - 1


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Inserting elements in a Binary Tree

# Creating a new node
# if node is empty say none, then root will be equal to new_node
# we create a temp variable known as the temp variable which is compared with elements in the tree
# while
#   if new_node  == temp return false : this is comparing an already existing element in the tree
#   if < left else > right : that is... if less then insert in  left or if greater then insert in right element
#   if there are no elements in the tree insert the new element else iterate to next

    def insert(self, value):
        new_node = Node(value)

        # In this first step ..we check if there a root node. If that node is none
        # Then we assign the value passed to us at the root node

        if self.root is None:
            self.root = new_node
            return True

        # if thats not the case, then we assign the value we have got in a temp variable

        temp = self.root

        # Then we start iterating over a loop checking all its part to check  where this value has to go

        while (True):

            # now if any of the node value is equal to the value which we have on temp variable then the return would be false. this means that value is duplicate
            # we could say that binary search tree does not accept duplicate values

            if new_node.value == temp.value:
                return False

            # Now we go to the core of the problem. We check if the value has to be added left or right
            # if the value is lower, then it goes to temp.left
            # then we return True meaning that node got insert

            if new_node.value < temp.value:

                # Now the goal is simple. You just need to add the value in the left node.
                # But there is a case where your left node might not be be there... you add this left node.
                # Else, you just simply add the value to the left node.

                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):

        # so if the root node is empty... it will return false. Meaning the tree itself is empty

        if self.root is None:
            return False

        # if its not the case, then temp will be taken as the root value

        temp = self.root

        # while the temp

        while temp is not None:

            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        # if the value you are checking for is not found, it means the value is not in the tree..
        return False
    # so it would break out of the code


my_tree = BinarySearchTree()


my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(1))
print(my_tree.contains(15))
