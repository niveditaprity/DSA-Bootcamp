def countNodesinLoop(head):
    #Your code here
    slow=head
    fast=head
    flag=0
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            flag=1
            break
        
    if flag==1:
        a1=slow
        count=0
        while a1.next!=slow:
            a1=a1.next
            count+=1
                
        return count+1
    return 0

