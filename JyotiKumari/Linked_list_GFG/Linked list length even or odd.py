def isLengthEvenOrOdd(head):
    # Code here
    count = 0
    while(head):
        count+=1
        head = head.next
    
    return not(count%2)