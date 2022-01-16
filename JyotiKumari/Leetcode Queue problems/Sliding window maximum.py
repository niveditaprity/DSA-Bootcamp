class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hold = deque()
        res = []
        n = len(nums)
        for i in range(k):
            while hold and nums[i] >= nums[hold[-1]] :
                hold.pop()
            hold.append(i)
        res.append(nums[hold[0]])
        
        for i in range(k, n):
            while hold and hold[0] <= i-k:
                hold.popleft()
            while hold and nums[i] >= nums[hold[-1]] :
                hold.pop()
            hold.append(i)
            res.append(nums[hold[0]])
        
        return res