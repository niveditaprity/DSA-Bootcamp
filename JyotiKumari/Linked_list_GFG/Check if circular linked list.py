def isCircular(head):
    # Code here
    if head==None:
        return True
    
    node = head.next
    
    while((node is not None) and (node is not head)):
        node = node.next
     
    return(node==head)