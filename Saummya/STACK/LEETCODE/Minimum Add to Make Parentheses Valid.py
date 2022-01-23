class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s=="":
            return 1
        
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == "(" and s[i] == ")":
                stack.pop(-1)
            else:
                stack.append(s[i])

        return len(stack)
