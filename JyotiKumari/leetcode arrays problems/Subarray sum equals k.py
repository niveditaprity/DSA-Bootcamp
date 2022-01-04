class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash = defaultdict(lambda: 0)
        s = 0
        count = 0
        
        for i in range(n):
            s += nums[i]
            if s == k:
                count += 1
            if (s - k) in hash:
                count += hash[s - k]
            hash[s] += 1
        return count
