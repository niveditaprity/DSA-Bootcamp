#User function Template for python3
from math import ceil
'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data   
        self.next = None
'''
        

def fractionalNodes(head,k):
        #add code here
        t = ceil(n/k)
        while(t>1):
            head = head.next
            t-=1
        return head