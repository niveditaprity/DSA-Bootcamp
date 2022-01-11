class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        S = list(s)
        stack = []
        for i in range(len(s)):
            if(S[i]=='('):
                stack.append(i)
            elif(S[i]==')'):
                if stack:
                    stack.pop()
                else:
                    S[i] = ""
        for i in stack:
            S[i] = ""
            
        return "".join(S)