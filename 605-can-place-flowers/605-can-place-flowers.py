class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new = [0] + flowerbed + [0]
        planted = 0
            
        for i in range(1, len(new)-1):
            if new[i-1] == 0 and new[i] == 0 and new[i+1] == 0:
                new[i] = 1
                planted +=1
                
        return planted >= n
            
            
        
            