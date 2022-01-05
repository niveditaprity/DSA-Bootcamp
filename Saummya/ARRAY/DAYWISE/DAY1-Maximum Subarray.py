class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = -inf
        global_max= -inf
        for i in range(len(nums)):
            current_max = max(0, current_max)
            current_max += nums[i]
            global_max = max(current_max, global_max)
        return global_max
