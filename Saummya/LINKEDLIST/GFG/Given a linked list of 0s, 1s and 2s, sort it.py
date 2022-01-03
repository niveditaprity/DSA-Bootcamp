class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        temp=head
        l1=[]
        while temp:
            l1.append(temp.data)
            temp=temp.next
            
        l1.sort()
        ll=LinkedList()
        for i in range(len(l1)):
            ll.append(l1[i])
            
        return ll.head
