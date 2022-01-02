def rotate(self, head, k):
        m=0
        n=head
        while n.next!=None:
            n=n.next
        tail=n
        curr=head
        while m<k:
            nxt=curr.next
            curr.next=None
            tail.next=curr
            tail=tail.next
            curr=nxt
            m+=1
        return curr
