class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordIndex = {ch: i for i,ch in enumerate(order)}
        for i in range(len(words)-1): # till second last index
            w1, w2 = words[i:i+2]
            
            for j in range(len(w1)): # iterating through word1
                
                # w2 is a prefix of w1 then return false
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    
                    # return False if order(word2) is less than order(word1)
                    if ordIndex[w1[j]] > ordIndex[w2[j]]:
                        return False
                    
                    # break if we found unequal words but order is correct
                    # to check next pair of words
                    break 
            
        return True