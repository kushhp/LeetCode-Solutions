class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        maxArea = 0
        while r >= l:
            maxArea = max(maxArea, (r-l) * min(height[l], height[r]))
            
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return maxArea
        