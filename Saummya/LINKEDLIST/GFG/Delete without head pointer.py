class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        temp=curr_node.next
        curr_node.data=temp.data
        curr_node.next=temp.next
