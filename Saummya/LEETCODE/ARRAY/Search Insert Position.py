class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #since o(logn) time complexity is mentioned, will use biinary search
        start=0
        end=len(nums)-1
        mid=0
        while start<=end:
            mid=(start+end)//2
            if target==nums[mid]:
                return mid
            if target<nums[mid]:
                end=mid-1
            elif target>nums[mid]:
                start=mid+1
        return start   #not in array, but start is intended index
