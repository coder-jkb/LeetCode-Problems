class Solution:
    remaining = {1: 1, 2: 2} # for future reference
    def climbStairs(self, n: int) -> int:
        # iterative approach
        if n in (1, 2):
            return n
        
        i, j = 1, 2
        count = 0
        while count<n-2:
            ans = i + j
            i = j
            j = ans
            count+=1
            
        return ans
