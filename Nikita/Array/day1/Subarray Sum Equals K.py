def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in nums:
            su += x
            ans += count[su-k]
            count[su] += 1
        return ans
