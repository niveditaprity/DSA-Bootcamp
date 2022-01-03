  def segregate(self, head):
        l=[]
        t=head
        while(t):
            l.append(t.data)
            t=t.next
        l.sort()
        l1=LinkedList()
        for i in range(len(l)):
            l1.append(l[i])
        return l1.head
