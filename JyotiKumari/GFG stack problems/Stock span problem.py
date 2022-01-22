class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        stack = [] 
        stack.append(0)
        ans = [0]*n
        ans[0] = 1
        for i in range(1, n):
            while( len(stack) > 0 and a[stack[-1]] <= a[i]):
                stack.pop()
            ans[i] = i + 1 if len(stack) <= 0 else (i - stack[-1])
            stack.append(i)
        
        return ans