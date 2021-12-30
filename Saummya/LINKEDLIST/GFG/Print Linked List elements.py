class Solution:
    def display(self,node):
        #code here
        while node:
            print( node.data, end=" ")
            node=node.next
