class Solution:
    def display(self,node):
        #code here
        while(node!=None):
            print(node.data, end = " ")
            node = node.next