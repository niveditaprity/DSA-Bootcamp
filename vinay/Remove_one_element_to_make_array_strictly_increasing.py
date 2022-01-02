class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        c=0
        n=len(nums)
        index=-1
        for i in range(n-1):
            if(nums[i]>=nums[i+1]):
                c+=1
                index=i
        if(c==0):
            return True
        if(c==1):
            if(index==0 or index==(n-2)):
                return True
            if(nums[index-1]<nums[index+1] or (index+2<n and nums[index]<nums[index+2])):
                return True
        return False
        
