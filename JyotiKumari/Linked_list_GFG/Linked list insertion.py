'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        # code here 
        temp=Node(x)
        if head==None:
            return temp
        temp.next=head
        head=temp
        return head
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        temp=Node(x)
        if head==None:
            return temp
        curr=head
        while curr.next:
            curr=curr.next
        curr.next=temp
        return head