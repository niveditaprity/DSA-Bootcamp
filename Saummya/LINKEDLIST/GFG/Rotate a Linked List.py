class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        temp = head
        prev = None
        while k:
            k -= 1
            prev = temp
            temp = temp.next
        if not temp:
            return head
        if prev:
            prev.next = None
        cur = temp
        while cur and cur.next:
            cur = cur.next
        if cur:
            cur.next = head
        return temp
        
