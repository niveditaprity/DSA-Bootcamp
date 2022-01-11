class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if char=='(':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    count+=1
        for c in stack:
            count+=1
        return count