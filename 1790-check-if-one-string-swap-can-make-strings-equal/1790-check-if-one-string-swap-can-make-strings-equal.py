class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        unequal_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                unequal_indices.append(i)
                
        
        length = len(unequal_indices)
        if length > 2 or length == 1:
            return False
               
        elif len(unequal_indices) == 0:
            return True
        
        elif s1[unequal_indices[0]] == s2[unequal_indices[1]] and s2[unequal_indices[0]] == s1[unequal_indices[1]]:
            return True
        
        return False
            