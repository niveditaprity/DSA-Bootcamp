class List:

    def __init__(self,data):
        self.data=data
        self.next=None

class MyStack:
    def __init__(self):
        self.root=None
    #Function to push an integer into the stack.
    def push(self, data):
        
        # Add code here
        newnode=List(data)
        newnode.next=self.root
        self.root=newnode
        return

    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if self.root is None:
            return -1
        else:
            temp=self.root
            self.root=self.root.next
            return temp.data