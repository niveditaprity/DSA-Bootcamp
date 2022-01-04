def union(head1,head2):
    # code here
    # return head of resultant linkedlist
    temp=head1
    temp1=head2
    s = set()
    
    while temp:
        if temp.data not in s:
            s.add(temp.data)
        temp = temp.next
        
    while temp1:
        if temp1.data not in s:
            s.add(temp1.data)
        temp1 = temp1.next
        
    l = []
    
    for i in s:
        l.append(i)
        
    l.sort()
    
    ll = linkedList()
    for i in l:
        ll.insert(i)
        
    return ll.head
