class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            # n - 1 not in seen, so n is the beginning of a sequence
            if (num - 1) not in seen:
                cur_length = 1
                while (num + cur_length) in seen:
                    cur_length += 1
                longest = max(longest, cur_length)

        return longest