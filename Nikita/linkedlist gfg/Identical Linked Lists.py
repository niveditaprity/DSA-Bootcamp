def areIdentical(head1, head2):
    while(head1 and head2):
        if head1.data!=head2.data:
            return False
        else:
            head1=head1.next
            head2=head2.next
    return True
