class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum_up_to_n = n * (n + 1) // 2

        return sum_up_to_n - sum(nums)