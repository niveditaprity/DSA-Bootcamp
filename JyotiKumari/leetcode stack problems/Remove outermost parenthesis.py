class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        stack = []

        for c in s:
            if (c == '('):
                if stack:
                    res+=c
                stack.append(c)
            else:
                stack.pop()
                if stack:
                    res+=c

        return res