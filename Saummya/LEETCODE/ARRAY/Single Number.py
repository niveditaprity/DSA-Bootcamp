class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_dict = defaultdict(int)
        for i in nums: 
            new_dict[i] += 1
        
        for j in new_dict: 
            if new_dict[j] == 1:
                return j
