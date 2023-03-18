class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        new = ""
        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys() and t[i] not in d.values():
                d[s[i]] = t[i]
                         
            try:
                new+=d[s[i]]
            except:
                pass
            
        return t == new
            
                