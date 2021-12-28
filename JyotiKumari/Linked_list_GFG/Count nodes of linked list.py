#Linked list class
'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        #code here
        temp = head_node
        count = 0 # Initialise count
  
        while (temp):
            count += 1
            temp = temp.next
        return count