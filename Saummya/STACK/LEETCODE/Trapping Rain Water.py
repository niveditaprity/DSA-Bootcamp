class Solution:
    def trap(self, height: List[int]) -> int:
        r = 0 
        
        for i in range(len(height)): 
            total = 0 
            if i>= 1 and i < len(height)-1:
                total = min(max(height[:i]), max(height[i+1:])) - height[i]
            if total > 0: 
                r += total 
        
        return r
