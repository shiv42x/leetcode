class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            # Left and right results
            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)
            
            # Compute cross sum
            left_sum = float('-inf')
            curr = 0
            for i in range(mid, left - 1, -1):
                curr += nums[i]
                left_sum = max(left_sum, curr)
            
            right_sum = float('-inf')
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                right_sum = max(right_sum, curr)
            
            cross_max = left_sum + right_sum
            
            return max(left_max, right_max, cross_max)
        
        return helper(0, len(nums) - 1)