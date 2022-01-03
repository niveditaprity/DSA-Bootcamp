def getNthFromLast(head,n):
    node = temp = head
    req = None
    count = 1
    while node:
        if count >= n:
            req = temp
            temp = req.next
        node = node.next
        count += 1
    if req:
        return req.data
    return -1
