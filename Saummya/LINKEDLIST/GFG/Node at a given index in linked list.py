def getNth(head, k):
    # Code here
    temp=head
    
    while k>1:
        temp=temp.next
        k-=1
    return temp.data
