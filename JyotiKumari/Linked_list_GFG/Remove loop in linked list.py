class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        slow_p = head
        fast_p = head
          
        while(fast_p!=None and fast_p.next!=None):
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if(fast_p==slow_p):
                break
            
        if(slow_p==head):
            while(slow_p.next!=fast_p):
                slow_p = slow_p.next
            slow_p.next = None
            
        if(fast_p==slow_p):    
            fast_p = head
            while(fast_p.next!=slow_p.next):
                fast_p = fast_p.next
                slow_p = slow_p.next
            slow_p.next = None