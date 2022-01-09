class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        s=[]
        for i in reversed(range(len(nums2))):
            # print(s)
            while s:
                if s[-1]<=nums2[i]:
                    s.pop()
                else:
                    res[nums2[i]] = s[-1]
                    break
            s.append(nums2[i])
        result=[]
        for i in nums1:
            if i in res:
                result.append(res[i])
            else:
                result.append(-1)
        return result
        
