class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [0]*n
        for i in range(n-2,-1,-1):
            while(stack and stack[-1]<=nums[i]):
                stack.pop()
            stack.append(nums[i])
        for i in range(n-1,-1,-1):
            while(stack and stack[-1]<=nums[i]):
                stack.pop()
            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans