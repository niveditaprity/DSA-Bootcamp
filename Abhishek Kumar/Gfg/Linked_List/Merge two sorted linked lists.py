def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(0)
    d1 = dummy
    h1 = head1
    h2 = head2
    while h1 and h2:
        if h1.data <= h2.data :
            d1.next = h1
            h1 = h1.next
            d1=d1.next
        elif h2.data < h1.data:
            d1.next = h2
            h2=h2.next
            d1=d1.next
    while h1:
        d1.next = h1
        h1=h1.next
        d1=d1.next
    while h2:
        d1.next = h2
        h2 = h2.next
        d1=d1.next
    return dummy.next
