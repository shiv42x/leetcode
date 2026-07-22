class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[0], heights[len(heights) - 1]
        total_water = 0

        # maxL - heights[i]
        # maxR - heights[i]
        while l < r:
            if maxL < maxR:
                total_water += maxL - heights[l]
                l += 1
                maxL = max(maxL, heights[l])
            else:
                total_water += maxR - heights[r]
                r -= 1
                maxR = max(maxR, heights[r])
        return total_water