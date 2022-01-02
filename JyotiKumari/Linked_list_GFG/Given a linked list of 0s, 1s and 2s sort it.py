class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        count = [0, 0, 0]
        ptr = head

        while ptr != None:
            count[ptr.data]+=1
            ptr = ptr.next
  
        i = 0
        ptr = head

        while ptr != None:
            if count[i] == 0:
                i+=1
            else:
                ptr.data = i
                count[i]-=1
                ptr = ptr.next
        return head