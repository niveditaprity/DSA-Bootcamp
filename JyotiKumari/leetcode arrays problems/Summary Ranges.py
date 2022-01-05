class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        curr = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                continue
            if curr == i:
                l.append(str(nums[curr]))
            else:
                l.append(str(nums[curr]) + "->" + str(nums[i]))
            curr = i+1
        
        return l