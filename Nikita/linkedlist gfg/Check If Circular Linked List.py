def isCircular(head):
    temp=head
    while(head):
        if(head.next==temp):
            return True
        head=head.next
    return False
        
    
