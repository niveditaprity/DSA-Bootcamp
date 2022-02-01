def rec_postOrder(root,lst):
    if root == None:
        return
    rec_postOrder(root.left,lst)
    rec_postOrder(root.right,lst)
    lst.append(root.data)
        
def postOrder(root):
    lst = []
    rec_postOrder(root,lst)
    return lst
