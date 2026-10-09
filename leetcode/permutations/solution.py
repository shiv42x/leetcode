class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(list(curr))
                return

            for num in nums:
                if num in curr:
                    continue   
                curr.append(num)
                backtrack(curr)
                curr.pop()

        backtrack([])
        return result