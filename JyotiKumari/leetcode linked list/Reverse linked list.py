class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head