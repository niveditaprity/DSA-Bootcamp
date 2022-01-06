class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_till_i = 0
        sums = {0:1}
        res = 0
        for num in nums:
            sum_till_i += num
            diff = sum_till_i - k
            if diff in sums:
                res += sums[diff]
            if sum_till_i in sums:
                sums[sum_till_i] += 1
            else:
                sums[sum_till_i] = 1
        return res
