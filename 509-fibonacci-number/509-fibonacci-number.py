class Solution:
    def fib(self, n: int) -> int:
        # iterative approach
        if n in (0, 1):
            return n
        
        i, j = 0, 1
        count = 0
        while count<=n-2:
            ans = i + j
            i = j
            j = ans
            count+=1
            
        return ans