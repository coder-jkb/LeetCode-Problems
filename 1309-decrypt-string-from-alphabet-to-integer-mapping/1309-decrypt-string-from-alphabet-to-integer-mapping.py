class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = 0
        while i<len(s):
            if i+2 < len(s) and s[i+2] == '#':
                val = int(s[i:i+2])
                i+=3
            else: 
                val = int(s[i])
                i+=1
                
            ans+=chr(97+val-1)
                
        return ans