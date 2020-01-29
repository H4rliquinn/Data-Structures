# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'BST:{self.value}\nL*{self.left}*\nR*{self.right}*'
    # Insert the given value into the tree

    def insert(self, value):
        curr_node = self
        new_node = BinarySearchTree(value)
        while True:
            if value > curr_node.value:
                if curr_node.right == None:
                    curr_node.right = new_node
                    break
                else:
                    curr_node = curr_node.right
            elif value < curr_node.value:
                if curr_node.left == None:
                    curr_node.left = new_node
                    break
                else:
                    curr_node = curr_node.left
            else:
                print("Anarchy!")
        return new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

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

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(6)
bst.insert(2)
print(bst)
bst.insert(17)
print(bst)
