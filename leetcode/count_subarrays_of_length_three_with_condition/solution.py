class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        num_subarrays = 0

        for i in range(1, len(nums) - 1):
            first = nums[i - 1]
            second = nums[i]
            third = nums[i + 1]

            if ((first + third) * 2) == second:
                num_subarrays += 1
        
        return num_subarrays