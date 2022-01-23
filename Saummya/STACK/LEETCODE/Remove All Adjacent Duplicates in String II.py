class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:       
                stack.append([i, 1])
                        
        ans = ""
        for i, j in stack:
            ans += i*j
        
        return ans
