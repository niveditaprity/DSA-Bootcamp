def minValue(root):
    ##Your code here
    if root==None:
        return -1
    
    while root.left != None:
        root = root.left 
        
    return root.data
