class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)
        if len(self.q1) == 1:
            return
        else:
            self.q2.append(self.q1.pop(0))
        

    def pop(self):
        """
        :rtype: nothing
        """
        top = self.q1.pop(0)
        for i in range(len(self.q2)-1):
            self.q1.append(self.q2.pop(0))
        self.q1, self.q2 =  self.q2, self.q1
        return top

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q1)==0 and len(self.q2)==0:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()