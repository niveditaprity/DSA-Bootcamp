def modularNode(head, k):
    count=0
    res=-1
    while(head):
        count+=1
        if count%k==0:
            res=head.data
        
        head=head.next
        
    return res
