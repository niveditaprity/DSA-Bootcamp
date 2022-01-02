def modularNode(head, k):
    #function should return the modular Node
    #if no such node is present then return -1
    temp=head
    count=0
    ans=-1
    while temp:
        count+=1
        if count%k==0:
            ans=temp.data
        temp=temp.next
        
    return ans
