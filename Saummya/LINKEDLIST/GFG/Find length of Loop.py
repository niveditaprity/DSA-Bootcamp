def countNodesinLoop(head):
    #Your code here
    slow=head
    fast=head
    c=0
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            c=1
            break
    if c==1:
        a1=slow
        count=0
        while a1.next!=slow:
            s1=a1.next
            count+=1
                
        return count
    return 0
