import sys
sys.path.append('../queue_and_stack/')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is found, return false to indicate no node inserted
        if self.value == value:
            pass
        # value smaller than node, look left
        elif value < self.value:
            # if node exists, continue recursively checking until something is found or inserted
            if self.left:
                return self.left.insert(value)
            # if no node exists, create new one and return true
            else:
                self.left = BinarySearchTree(value)
                return(value,'Added')
        else:
            # if node exists, continue recursively checking until something is found or inserted
            if self.right:
                return self.right.insert(value)
            # if no node exists, create new one and return true
            else:
                self.right = BinarySearchTree(value)
                return(value,'Added')
    
    def contains(self, target):
        if target== self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
            
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        elif self.right:
            return self.right.get_max()
        print(self.value)
        
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
         # if right node exists, perform function again
        if self.right:
            self.right.for_each(cb)
        # if left node exists, perform function again
        if self.left:
            self.left.for_each(cb)
        # perform function once you reach the end node
        cb(self.value)
        
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
