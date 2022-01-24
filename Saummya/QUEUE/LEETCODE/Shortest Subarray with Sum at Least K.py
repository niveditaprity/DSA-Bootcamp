class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        lst = []
        
        for i, j in itertools.combinations(range(len(nums) + 1), 2):
            lst.append(nums[i:j])
        
        res = []
        for i in sorted(lst):
            if sum(i) >=k:
                res.append(i)
              
        res.sort(key = lambda x:len(x))
        if res:
            return (len(res[0]))
        else:
            return -1
