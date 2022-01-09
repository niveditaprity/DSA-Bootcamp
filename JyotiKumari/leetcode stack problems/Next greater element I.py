class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        hash_set = {}
        ans = []
        for i in range(n-1,-1,-1):
            while(stack and stack[-1]<nums2[i]):
                stack.pop()
            if not stack:
                hash_set[nums2[i]] = -1
            else:
                hash_set[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for num in nums1:
            ans.append(hash_set[num])
            
        return ans