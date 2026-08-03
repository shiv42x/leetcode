class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_yet = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest_yet = max(longest_yet, r - l + 1)

        return longest_yet