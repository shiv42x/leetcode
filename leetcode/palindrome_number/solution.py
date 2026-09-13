class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if 0 <= x <= 9: 
            return True
        
        number = x
        reverse = 0
        
        while number: 
            reverse = reverse * 10 + number % 10
            number = number // 10 
        
        return x == reverse