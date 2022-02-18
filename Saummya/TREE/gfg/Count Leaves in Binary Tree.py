'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def countLeaves(root):
    # Code here
    if root is None:
        return 0
 
    if root.left is None and root.right is None:
        return 1      
    return countLeaves(root.left) + countLeaves(root.right)
       
