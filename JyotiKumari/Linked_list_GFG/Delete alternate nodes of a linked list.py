class Solution: 
    
    
    def deleteAlt(self, head):
        
        #add code here
        prev = head 
        now = head.next
  
        while (prev != None and now != None): 
            prev.next = now.next
            now = None
            prev = prev.next
            if (prev != None): 
                now = prev.next