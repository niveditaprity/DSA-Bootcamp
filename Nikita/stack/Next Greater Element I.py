class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater,stack = {},[]
        for n in nums2:
            while stack and n > stack[-1]:
                greater[stack.pop()] = n
            stack.append(n)
        return [greater[n] if n in greater else -1 for n in nums1]
