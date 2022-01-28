class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        right = 0
        while(right<len(nums)):
            if (nums[right] == 0):
                k-=1
            if (k< 0):
                if (nums[left] == 0):
                    k+=1
                left+=1
            right+=1

        return right - left