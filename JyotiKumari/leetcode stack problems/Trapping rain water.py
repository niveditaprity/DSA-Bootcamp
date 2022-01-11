class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = n*[0]
        right = n*[0]
        water = 0
        max_so_far_left = height[0]
        left[0] = height[0]
        for i in range(1,n):
            if height[i]>max_so_far_left:
                max_so_far_left = height[i]
            left[i] = max_so_far_left
        max_so_far_right = height[-1]
        for i in range(n-1,-1,-1):
            if height[i]>max_so_far_right:
                max_so_far_right = height[i]
            left[i] = min(left[i],max_so_far_right)
            water = water + left[i]-height[i]
            
        return water