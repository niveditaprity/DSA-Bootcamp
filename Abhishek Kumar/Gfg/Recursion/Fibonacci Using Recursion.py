class Solution:
    def fibonacci(self,n):
        if n < 2:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)
