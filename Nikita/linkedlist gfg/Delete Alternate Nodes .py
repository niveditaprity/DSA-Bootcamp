    
    def deleteAlt(self, head):
        temp = head
        while temp!= None and temp.next != None:
            temp.next = temp.next.next
            temp= temp.next
              
                
