class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1:
            return False
        stack= []
        brackets=  {")": "(", "}": "{", "]": "["}

        for i in range(len(s)):
            if s[i] not in brackets.keys():
                stack.append(s[i])
            else:
                if (len(stack) > 0) and stack[-1] == brackets[s[i]]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0