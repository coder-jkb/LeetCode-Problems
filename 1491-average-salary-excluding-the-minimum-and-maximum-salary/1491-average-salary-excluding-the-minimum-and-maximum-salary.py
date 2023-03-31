class Solution:
    def average(self, salary: List[int]) -> float:
        mins, maxs = float('inf'), float('-inf')
        total = 0
        n = 0
        for s in salary:
            if s < mins:
                mins = s
                
            if s > maxs:
                maxs = s
            
            total += s
            n+=1
        return (total-mins-maxs)/(n-2)