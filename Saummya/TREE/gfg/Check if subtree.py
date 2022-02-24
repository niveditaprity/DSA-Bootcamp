

'''

class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case


class Solution:
    def isSubTree(self, T, S):
        # Code here
                
        if T == S:
            return True
 
        if T is None:
            return False

        first = []
        second = []
     
        self.inorder(T, first)
        self.inorder(S, second)
     
        if not self.is_sublist(first, second):
            return False
     
        first.clear()
        second.clear()
     
        self.postorder(T, first)
        self.postorder(S, second)
     
        if not self.is_sublist(first, second):
            return False
     
        return True
        
    def inorder(self, node, list):
        if node is None:
            list.append(0)
            return
     
        self.inorder(node.left, list)
        list.append(node.data)
        self.inorder(node.right, list)
        
    def postorder(self, node, list):
        if node is None:
            list.append(0)
            return
     
        self.postorder(node.left, list)
        self.postorder(node.right, list)
        list.append(node.data)
        
    def is_sublist(self, x, y):
        for i in range(len(x) - len(y) + 1):
            if x[i: i + len(y)] == y:
                return True
        return False
