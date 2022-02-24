'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# your task is to complete this function
# function should return True is Tree is SumTree else return False
def ss(root):
    if root is None:
        return 0
    return ss(root.left)+root.data+ss(root.right)


class Solution:
    def isSumTree(self,root):
        # Code here
        if root is None or (root.left is None and root.right is None):
            return 1
        ls = ss(root.left)
        rs = ss(root.right)
        if root.data == ls+rs and self.isSumTree(root.left) and self.isSumTree(root.right):
            return 1
        return 0
