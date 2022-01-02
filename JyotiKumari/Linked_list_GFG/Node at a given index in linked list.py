def getNth(head, k):
    # Code here
    count = 1
    while(count<k):
        head = head.next
        count+=1
    return head.data