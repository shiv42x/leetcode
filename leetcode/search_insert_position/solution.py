class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = -1
        r = len(nums)

        while (r - l) > 1:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
    
        if r < len(nums) and nums[r] == target:
            return r
            
        return l + 1