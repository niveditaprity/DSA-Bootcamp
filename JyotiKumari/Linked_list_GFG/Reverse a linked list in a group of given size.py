class Solution:
    def reverse(self,head, k):
        # Code here
        if head == None:
            return head
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse(next, k)
 
        return prev