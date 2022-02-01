class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        for num in nums:
            if num in lookup:
                lookup[num]+=1
            else:
                lookup[num] = 1
        i = 0
        ans = []
        for key, value in reversed((sorted(lookup.items(), key = lambda x:x[1] ))):
            if(i==k):
                break
            ans.append(key)
            i+=1
            
        return ans