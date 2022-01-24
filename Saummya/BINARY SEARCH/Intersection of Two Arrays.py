class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        res=set()
        for i in range(n2):
            if nums2[i] in nums1:
                res.add(nums2[i])
        return list(res)
                
