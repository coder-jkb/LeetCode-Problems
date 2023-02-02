class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==1 or x==0:
            return x
        
        if n==0:
            return 1
        elif n>0:
            ans = self.myPow(x*x, n//2)
            if n%2==0:
                return ans
            else:
                return x*ans
            # return x * self.myPow(x, n-1)
        
        else:
            return 1 / self.myPow(x, abs(n))