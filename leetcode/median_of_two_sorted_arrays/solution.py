class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            partX = (low + high) // 2
            partY = total_left - partX
            
            maxLeftX = nums1[partX - 1] if partX > 0 else float('-inf')
            minRightX = nums1[partX] if partX < m else float('inf')
            
            maxLeftY = nums2[partY - 1] if partY > 0 else float('-inf')
            minRightY = nums2[partY] if partY < n else float('inf')
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 1:
                    return float(max(maxLeftX, maxLeftY))
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            elif maxLeftX > minRightY:
                high = partX - 1
            else:
                low = partX + 1
                
        return 0.0