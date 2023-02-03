class Solution:
    remaining = {1: 1, 2: 2} # for future reference
    def climbStairs(self, n: int) -> int:
        if n in Solution.remaining:
            return Solution.remaining[n]
        else:
            ways = self.climbStairs(n-1) + self.climbStairs(n-2)
            Solution.remaining[n] = ways
            return ways 
