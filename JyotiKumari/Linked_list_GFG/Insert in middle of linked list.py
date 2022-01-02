def insertInMid(head,node):
    #code here
    first = head
    second = head.next
    while second and second.next:
        first = first.next
        second = second.next.next
    node.next = first.next
    first.next = node