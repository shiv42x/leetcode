class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        greatest_yet = 0

        while l < r:
            curr_amount = min(height[l], height[r]) * (r - l)
            greatest_yet = max(greatest_yet, curr_amount)
            
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1

        return greatest_yet
        