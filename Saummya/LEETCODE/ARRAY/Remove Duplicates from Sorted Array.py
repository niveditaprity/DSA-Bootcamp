class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[0]
        for i in range(0,len(nums)-2,1):
            if nums[i]==nums[i+1]:
                del nums[i] 
        return len(nums)
