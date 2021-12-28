def getCount(self, head_node):
        count=0
        while(head_node):
            head_node=head_node.next
            count+=1
        return count
