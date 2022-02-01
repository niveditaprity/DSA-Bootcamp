def rec_preorder(root,lst):
    if root==None:
        return
    lst.append(root.data)
    rec_preorder(root.left,lst)
    rec_preorder(root.right,lst)
    
def preorder(root):
    lst = []
    rec_preorder(root,lst)
    return lst
