class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()
        res = []
        i,j=0,0
        while j<len(nums):
            d.append(nums[j])
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                res.append(max(d))
                d.popleft()
                i+=1
                j+=1
        return res
