class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = []

    def push(self, val: int) -> None:
        if(not self.stack or val<=self.curr_min[-1]):
            self.curr_min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if(self.stack[-1]==self.curr_min[-1]):
            self.curr_min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()