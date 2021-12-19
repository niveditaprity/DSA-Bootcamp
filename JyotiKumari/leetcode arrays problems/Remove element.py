class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        index = 0
        count = len(nums)
        for i in range(len(nums)):
            if(val==nums[i]):
                nums[i] = '_'
                count = count-1
        j = 0
        for i in range(len(nums)):
            if(nums[i]!='_'):
                nums[j] = nums[i]
                j+=1
            if(i>=count):
                nums[i] = '_'
        return count