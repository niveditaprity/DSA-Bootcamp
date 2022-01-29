class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<r):
            mid=(l+r)//2
            if(target==nums[mid]):
                return mid
            elif(target>nums[mid]):
                l=mid+1
            elif(target<nums[mid]):
                r=mid-1
        if(l==r and target==nums[l]):
            return l
        return -1
        
