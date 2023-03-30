class Solution:
    def fib(self, n: int) -> int:
        # iterative approach
        if n in (0, 1):
            return n
        
        ans = 1
        i, j = 0, 1
        count = 0
        while count<n-2:
            i = j
            j = ans
            ans = i + j
            count+=1
            
        return ans