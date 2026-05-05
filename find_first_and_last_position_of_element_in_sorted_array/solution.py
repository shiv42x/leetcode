class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        result = [-1, -1]

        for i, num in enumerate(nums):
            # if target, and first occurence not found
            if num == target and result[0] == -1:
                result[0] = i
            # if target, and first occurence found, keep updating (it stops updating at last element)
            if num == target and result[0] != -1:
                result[1] = i

        #return result

        # O(log n)
        def bin_search(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        left = bin_search(nums, target)
        
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        # search for target + 1, return one idx less than that 
        right = bin_search(nums, target + 1) - 1
        
        return [left, right]