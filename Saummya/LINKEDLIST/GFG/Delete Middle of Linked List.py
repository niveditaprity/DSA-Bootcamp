def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    #code here
    #Approach1
    '''
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        
    nodetodel=slow
    temp=head
    while nodetodel > 1:
        temp = temp.next
        nodetodel-= 1 
    temp.next =temp.next.next
    
    return temp
    '''
    
    #Approach2
    
    lengthofLL = getlength(head)
    
    if lengthofLL == 1:
        return 
        
    nodetodel = lengthofLL//2
    
    currentnode = head
    while nodetodel > 1:
        currentnode = currentnode.next
        nodetodel -= 1 
    currentnode.next = currentnode.next.next
    
    return head
    
def getlength(head):
    length = 0
    currentnode = head
    while currentnode is not None:
        length += 1
        currentnode = currentnode.next
    return length
