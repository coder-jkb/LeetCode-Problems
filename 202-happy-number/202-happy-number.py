class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while True:
            if n == 1:
                return True
            elif n not in seen:
                seen.append(n)
                n = self.sqrOfDigs(n)
            else: # number started repeating
                return False

    def sqrOfDigs(self,n):
        sumofsqr = 0
        while n > 0:
            sumofsqr+=(n%10)**2
            n = n//10
        return sumofsqr