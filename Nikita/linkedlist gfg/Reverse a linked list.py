def reverseList(self, head):
        prev=None
        temp=None
        while(head):
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        head=prev
        return head
