class Solution:
    def isPalindrome(self, x: int) -> bool:
        cpy = x
        new = 0
        while x > 0:
            new = new*10 + x%10
            x = x//10
            
        return new == cpy