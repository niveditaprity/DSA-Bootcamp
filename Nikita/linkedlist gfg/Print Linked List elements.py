def display(self,node):
        data=[]
        while(node):
            data=node.data
            node=node.next
            print(data,end=" ")
