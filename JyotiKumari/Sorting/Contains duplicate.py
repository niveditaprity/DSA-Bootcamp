class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        flag = 0
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                flag = 1
                break
        if(flag):
            return True
        return False