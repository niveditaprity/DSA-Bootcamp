class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        result = set()
        look = set()
        for num in nums:
            if num-k in look:
                result.add(num-k)
            if num+k in look:
                result.add(num)
            look.add(num)
        return len(result)