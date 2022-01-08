class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for char in s:
            if char!='#':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        s = "".join(stack)
        stack = []
        for char in t:
            if char!='#':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        t = "".join(stack)
        
        return s==t