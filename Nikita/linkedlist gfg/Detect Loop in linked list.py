def detectLoop(self, head):
        temp = head
        while head and head.next:
           
            if temp.next == None:
                return False
            elif temp.next == head:
                return True
               
            temp = temp.next
           
        return False
