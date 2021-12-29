def insertInMid(head,node):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    node.next = slow.next
    slow.next = node
