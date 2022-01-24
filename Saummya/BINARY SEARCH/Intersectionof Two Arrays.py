#USING BINARY SEARCH APPROACH
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def binarySearch(nums,target):
            n=len(nums)
            start=0
            end=n-1

            while(start<=end):
                mid=(start+end)//2
                if (nums[mid]==target):
                    return mid
                elif nums[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            return -1
        
        
        n1=len(nums1)
        n2=len(nums2)
        longLenArray=nums1 if n1>=n2 else nums2
        shortLenArray=nums2 if n1>=n2 else nums1
        longLenArray.sort()
        res=set()
        for ele in shortLenArray:
            if binarySearch(longLenArray,ele):
                res.add(ele)
        return res
      
      
      #--------------------------------------------------------------------------
      #APPROACH-2--------------------------
      #----------------------------------------------------------------------------
      #LINEAR SEARCH APPROACH
      class Solution:
        def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
            n1=len(nums1)
            n2=len(nums2)
            res=set()
            for i in range(n2):
                if nums2[i] in nums1:
                    res.add(nums2[i])
            return list(res)
