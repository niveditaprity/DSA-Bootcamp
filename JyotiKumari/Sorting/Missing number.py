class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        flag = 0
        for i in range(len(nums)):
            if(nums[i]!=i):
                flag = 1
                break
        if(flag):
            return i
        return len(nums)