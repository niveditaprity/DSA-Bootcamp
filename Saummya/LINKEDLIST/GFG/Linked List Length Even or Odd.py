def isLengthEvenOrOdd(head):
    # Code here
    count=0
    while head:
        count+=1
        head=head.next
        
    if count%2==0:
        return True
    else:
        return False
