class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=(len(haystack) - len(needle) + 1)

        for i in range(n):
            if haystack[i:i+len(needle)]==needle:
                return i

        return -1