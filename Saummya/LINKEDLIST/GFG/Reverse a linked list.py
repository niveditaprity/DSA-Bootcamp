class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while(curr.next):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        head = curr
        return head
