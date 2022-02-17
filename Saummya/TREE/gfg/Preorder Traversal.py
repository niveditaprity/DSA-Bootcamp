
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    a=[]
    preorder1(root,a)
    return a
    
    
def preorder1(root,a):
    if root:
        a.append(root.data)
        preorder1(root.left,a)
        preorder1(root.right,a)
