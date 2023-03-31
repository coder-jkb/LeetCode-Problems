class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        index = -1
        for ind, (i, j) in enumerate(points):
            if x==i or y==j:
                dist = abs((x-i)+(y-j))
                if dist < min_dist:
                    min_dist = dist
                    index = ind
        return index