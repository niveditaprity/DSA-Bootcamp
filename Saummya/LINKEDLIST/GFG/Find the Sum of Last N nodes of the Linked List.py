#approach1

def sumOfLastN_Nodes(head,n):
    #function should return sum of last n nodes
    if n<=0:
        return 0
    temp=head
    count=1
    while count!=n:
        temp=temp.next
        count+=1
    temp=temp.next
    sum1=0
    while temp:
        sum1+=temp.data
    return sum1
        
    
    
 #APPROACH 2
def sumOfLastN_Nodes(head,n):
    #function should return sum of last n nodes
    if n<=0:
        return 0
    temp=head
    ele_count=0
    while temp!=None:
        temp=temp.next
        ele_count+=1
    
    n1=ele_count-n-1
    if n1<=0:
        return 0
    temp1=head
    count=0
    while count!=n1:
        count+=1
        temp1=temp1.next
    temp1=temp1.next
    sum1=0
    while temp1!=None:
        sum1+=temp1.data
        temp1=temp1.next
        
    return sum1
        
    
 #APPROACH 3
#FINAL APPROACH
def sumOfLastN_Nodes(head,n):
    #function should return sum of last n nodes
    temp=head
    size=0
    while temp!=None:
        size+=1
        temp=temp.next
    temp=head
    
    
    sum1=0
    while temp!=None:
        if size<=n:
            val=temp.data
            sum1+=val
        size-=1
        temp=temp.next
    return sum1
