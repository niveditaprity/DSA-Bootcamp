class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        S= list(s)
        stack = []
        for i, c in enumerate(S):
            if c == ")":
                if stack:
                    stack.pop()
                else: 
                    S[i] = ""
            elif c == "(":
                stack.append(i)
        for i in stack: 
            S[i] = ""
