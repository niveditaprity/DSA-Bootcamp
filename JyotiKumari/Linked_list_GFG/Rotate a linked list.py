# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if k == 0:
            return
        
        current = head
        count = 1
        
        while(count <k and current != None):
            current = current.next
            count += 1
    
        if current is None:
            return

        kNode = current

        while(current.next is not None):
            current = current.next

        current.next = head
        head = kNode.next
        kNode.next = None
        return head