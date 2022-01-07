"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        # code here
        
        '''
        if head==None and head.next==None:
            return head
        newNode=head.next
        prev=head
        prev.next=newNode.next
        newNode.next=prev
        prev.next=pairwiseSwap(prev.next)
        return newNode
        '''
        '''
        temp=head
        while temp.next.next:
            d1=temp.val
            d2=temp.next.val
            temp.val=d2
            temp.next.val=d1
            temp=temp.next.next
        return head
        '''
        
        #-----APPROACH2--------
        prev, first = None, head
        while first and first.next:
            second = first.next
            third = first.next.next
                
            if prev:
                prev.next = second
                second.next = first
                first.next = third
            else: # First two nodes
                head = second
                second.next = first
                first.next = third
            prev = first
            first = first.next
        
        return head
      
