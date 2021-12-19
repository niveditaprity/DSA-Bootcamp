class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        s=sum(nums[:k])
        res=s/k
        
        prefix=[0]*(n)
        prefix[0]=nums[0]
        
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        
        for i in range(k,n):
            s=prefix[i]-prefix[i-k]
            res=max(res,s/k)
        
        return res
            
            
            
