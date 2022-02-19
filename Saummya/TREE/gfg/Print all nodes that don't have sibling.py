#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    # code here
    def traversal(root):
        #l1=[]
        if root is None:
            return None
        
        if root.left and root.right is None:
            l1.append(root.left.data)
        
        if root.right and root.left is None:
            l1.append(root.right.data)
        
        if root.left:
            traversal(root.left)
            
        if root.right:
            traversal(root.right)
            
    l1=[]
    traversal(root)
    if l1==[]:
        return [-1]
    return sorted(l1)
