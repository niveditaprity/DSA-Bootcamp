#User function Template for python3


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here
        tr=[]
        if root:
            return(self.InOrder(root.left) + [root.data] +self.InOrder(root.right))
        else:
            return []
