class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 1, x // 2
        
        while left < right:
            mid = left + (right - left + 1) // 2
            
            if mid <= x // mid:
                left = mid 
            else:
                right = mid - 1
                
        return left
