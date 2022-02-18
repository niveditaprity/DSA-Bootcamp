# Your task to complete this function
# function should return size of the binary tree as integer
def getSize(node):
    # code here
    if node is None:
        return 0
    ls=getSize(node.left)
    rs=getSize(node.right)
    
    return ls+rs+1
