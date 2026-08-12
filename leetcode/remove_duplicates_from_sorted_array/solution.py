class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        overwrite_idx = 1

        for i in range(1, n):
            # check if duplicate or unique 
            # nums[i] (current) will be unique if nums[i - 1] (previous) is not the same
            # if unique, can overwrite at overwrite_idx
            if nums[i] != nums[i - 1]:
                nums[overwrite_idx] = nums[i]
                overwrite_idx += 1

        return overwrite_idx