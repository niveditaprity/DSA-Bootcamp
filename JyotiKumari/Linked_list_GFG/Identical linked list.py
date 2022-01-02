def areIdentical(head1, head2):
    # Code here
    t1 = head1
    t2 = head2
    while(t1!=None and t2!=None):
        if(t1.data!=t2.data):
            return False
        t1 = t1.next
        t2 = t2.next
        
    #If linked lists are identical then t1 and t2 must be empty now.
    return (t1==None and t2==None)