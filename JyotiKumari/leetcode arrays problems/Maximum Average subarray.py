class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if(k>n):
            return -1
        
        s = 0
        for i in range(k):
            s+=nums[i]
        max_sum = s
        for i in range(k,n):
            s+=nums[i]-nums[i-k]
            if(s>max_sum):
                max_sum = s
        return max_sum/k