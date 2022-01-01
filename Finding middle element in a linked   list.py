def findMid(self, head):
        count=0
        t=head
        while(t):
            count+=1
            t=t.next
        i=0
        t=head
        while(i<count//2):
            t=t.next
            i+=1
        return t.data
        
        
