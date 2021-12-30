def getNth(head, k):
    c=0
    while(head):
        c+=1
        if(c==k):
            return head.data
        head=head.next
