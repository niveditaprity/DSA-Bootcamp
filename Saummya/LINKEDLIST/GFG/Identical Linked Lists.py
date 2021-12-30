def areIdentical(head1, head2):
    # Code here
    c1=head1
    c2=head2
    
    while (c1 and c2):
        if c1.data!=c2.data:
            return False
        c1=c1.next
        c2=c2.next
    if c1 is None and c2 is None:
        return True
    else:
        return False
