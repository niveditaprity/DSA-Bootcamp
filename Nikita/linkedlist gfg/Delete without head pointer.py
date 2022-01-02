def deleteNode(self,curr_node):
        next=curr_node.next
        curr_node.data=next.data
        curr_node.next=next.next
        #code here
