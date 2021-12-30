import math
def fractionalNodes(head,k):
        #add code here
        i = 0
        if head is not None:
            while head:
                i+=1
                if i == math.ceil(n/k):
                    return head
                else:
                    head = head.next
        
