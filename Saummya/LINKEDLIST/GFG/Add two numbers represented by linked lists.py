class Solution:
    #Function to add two numbers represented by linked list.
    def reverse(self, head):
            prev = None
            temp = head
            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            head = prev
            
            return head
    
    
    
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        sum1=0
        carry=0
        dummy=Node(-1)
        temp=dummy
        first = self.reverse(first)
        second = self.reverse(second)
        
        while(first is not None or second is not None or carry !=0):
            s = 0
            if first is not None:
                s += first.data
                first = first.next
            if second is not None:
                s += second.data
                second = second.next
                
            s += carry
            carry = s//10
            
            temp.next = Node(s%10)
            temp = temp.next
