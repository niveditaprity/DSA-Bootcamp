class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if(stack and stack[-1][0]==s[i]):
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
                continue
            stack.append([s[i],1])
        ans = ""
        for key, value in stack:
            ans+=key*value
        return ans
            