class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        n=0
        while temp:
            temp=temp.next
            n+=1
        for i in range(n//2):
            head=head.next
        return head
