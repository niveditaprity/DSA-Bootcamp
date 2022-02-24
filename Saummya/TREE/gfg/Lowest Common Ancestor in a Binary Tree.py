
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root
    
        leftLCA = self.lca(root.left,n1,n2)
        rightLCA = self.lca(root.right,n1,n2)
        
        if leftLCA and rightLCA:
            return root
        if leftLCA:
            return leftLCA
        else:
            return rightLCA
        
