class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        out = [[]]
        for n in nums:
            out += [curr + [n] for curr in out]
        return out