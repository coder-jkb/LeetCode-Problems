class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)
        
        def slope(p1,p2):
            x1, y1 = p1
            x2, y2 = p2
            
            if x2-x1 != 0:
                return (y2-y1)/(x2-x1)
            return float('inf')
        
        for i in range(1,length-1):
            p0 = coordinates[i-1]
            p1 = coordinates[i]
            p2 = coordinates[i+1]
            if slope(p0, p1) != slope(p1,p2):
                return False
            
        return True