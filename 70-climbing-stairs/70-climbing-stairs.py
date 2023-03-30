class Solution:
    remaining = {1: 1, 2: 2} # for future reference
    def climbStairs(self, n: int) -> int:
        if n not in Solution.remaining:
            Solution.remaining[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return Solution.remaining[n] 
