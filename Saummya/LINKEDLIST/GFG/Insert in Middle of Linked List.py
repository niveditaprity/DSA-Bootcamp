def insertInMid(head,node):
    #code here
    temp = head
    temp1 = head
    while temp1.next != None and temp1.next.next != None:
        temp = temp.next
        temp1 = temp1.next.next
    node.next = temp.next
    temp.next = node
