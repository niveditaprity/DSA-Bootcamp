class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = [sum(nums[0:k])]

        n = len(nums)
        for i in range(1, n-k+1):
            sums.append(sums[i-1] - nums[i - 1] + nums[k + i - 1])
        return max(sums) / k
