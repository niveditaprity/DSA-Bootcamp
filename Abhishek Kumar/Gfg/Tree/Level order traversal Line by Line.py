def levelOrder(root):
    
    # code here
    if root == None:
        return
    lst = []
    q = []
    q.append(root)
 
    while len(q) > 0:
        count = len(q)
        temp = []
        for i in range(count):
            curr=q.pop(0)
            temp.append(curr.data)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        lst.append(temp)
    return lst
