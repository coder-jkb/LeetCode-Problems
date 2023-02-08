from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dd = defaultdict(list)
        
        for s in strs:
            s2 = str(sorted(s))
            dd[s2].append(s)
            
        return [val for _, val in dd.items()]