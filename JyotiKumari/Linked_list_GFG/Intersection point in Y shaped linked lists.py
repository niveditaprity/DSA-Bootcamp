def intersetPoint(head1,head2):
    #code here
    if(head1==None or head2==None):
        return None
    a = head1
    b = head2
    while(a!=b):
        a = a.next
        b = b.next
        if(a is None):
            a = head2
            a = a.next
        if(b is None):
            b = head1
            b = b.next
    return a.data