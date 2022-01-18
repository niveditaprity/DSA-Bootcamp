from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = deque()
        for i in range(n):
            circle.appendleft(i+1)
        while(len(circle)>1):
            t = k-1
            while(t):
                temp = circle.pop()
                circle.appendleft(temp)
                t-=1
            circle.pop()
        return circle[0]