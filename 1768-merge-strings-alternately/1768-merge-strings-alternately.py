class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        i = 0
        diff = len(word1) - len(word2)
        if diff <= 0:
            shorter, longer = word1, word2
            
        else:
            shorter, longer = word2, word1
            
        
        for i in range(0,len(shorter)):
            # print(word1[i] + word2[i], new)
            new += word1[i] + word2[i]
        
        if diff != 0:
            new+=longer[i+1:]
            
        return new