class Solution:
    def delete(self,head, del_):
        if (head == None or del_ == None):
            return
     
        if (head == del_):
            head = del_.next

        if (del_.next != None):
            del_.next.prev = del_.prev

        if (del_.prev != None):
            del_.prev.next = del_.next
             
        return head
    
    def deleteNode(self,head, x):
        # Code here
        if (head == None or x <= 0):
            return
 
        current = head
        i = 1
        
        while ( current != None and i < x ):
            current = current.next
            i = i + 1
     
        if (current == None):
            return
     
        self.delete(head, current)
         
        return head