#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    
    count=0
    temp=head
    while temp:
        count+=1
        temp=temp.next
        
    if n>count:
        return -1
        
    i=0
    temp=head
    while (i<count-n):
        temp=temp.next
        i+=1
        
    return temp.data
        
    
    
    '''
    #APPROACH2 
    
    
    slow = head
    fast = head
    
    for i in range(n):
        if not fast:
            return -1
        fast = fast.next
        
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.data
    '''
    
    
