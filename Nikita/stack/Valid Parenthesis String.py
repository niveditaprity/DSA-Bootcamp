class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            elif c == "*":
                low -= 1
                high += 1
            low = max(low, 0)
            if(high < 0):
                return False 
        return low == 0
