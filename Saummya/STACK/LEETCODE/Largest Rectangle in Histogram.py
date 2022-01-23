class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left, stack = [0] * n, []
        for i in range(n):
            h, start = heights[i], i
            while stack and h <= heights[stack[-1]]:
                start = stack.pop()

            left[i] = (i - start) + left[start]
            stack.append(i)
            
            #---------------

        right, stack = [0] * n, []
        for i in reversed(range(n)):
            h, end = heights[i], i
            while stack and h <= heights[stack[-1]]:
                end = stack.pop()
            
            right[i] = (end - i) + right[end]
            stack.append(i)
           
        #--------------

        area = 0
        for i, height in enumerate(heights):
            width = right[i] + left[i] + 1
            area = max(area, width * height)
        return area
      
      
      '''
      Time complexity: O(N)
      Space complexity: O(N)
      ref explanation:
      https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/1690792/Stack-based-O(N)-with-detailed-explanation
      '''
      
