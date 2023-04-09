class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        s = sorted(s)
        t = sorted(t)
        while i < len(s):
            if s[i] != t[i]:
                return t[i]
            
            i+=1
            
        return t[-1]