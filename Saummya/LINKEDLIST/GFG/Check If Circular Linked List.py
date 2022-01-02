def isCircular(head):
    # Code here
    temp=head
    flag=0
    while temp:
        if temp.next==head:
            flag=1
            break
        temp=temp.next
        
    if flag:
        return 1
    else:
        return 0
