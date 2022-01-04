class Solution:    
    def pairWiseSwap(self, head):
        # code here
        if(head is None or head.next is None):
            return head
        
        curr=head.next
        head.next = self.pairWiseSwap(head.next.next)
        curr.next = head
        return curr