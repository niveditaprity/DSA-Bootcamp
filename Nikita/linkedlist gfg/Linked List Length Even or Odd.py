def isLengthEvenOrOdd(head):
    count=0
    while(head):
        count+=1
        head=head.next
    if count%2==0:
        return 1
    else:
        return 0
