class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in s[::-1]:
            if length > 0 and char == ' ':
                break

            if char == ' ':
                continue
            else:
                length += 1

        return length