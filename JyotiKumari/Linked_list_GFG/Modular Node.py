#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def modularNode(head, k):
    #function should return the modular Node
    #if no such node is present then return -1
    ans = -1
    ind = 1
    while(head!=None):
        if(ind%k==0):
            ans = head.data
        ind+=1
        head = head.next
    return ans