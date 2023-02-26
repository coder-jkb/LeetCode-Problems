class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        saved = dict()
        def helper(i,j):
            if (i,j) in saved:
                return saved[(i,j)]
            
            if i==m-1 and j==n-1:
                saved[(i,j)] = 1
            
            elif j==n-1:
                saved[(i, j)] = helper(i+1, j)
            
            elif i==m-1:
                saved[(i, j)] = helper(i,j+1)
            
            else:
                saved[(i, j)] = helper(i, j+1)+helper(i+1, j)
            
            return saved[(i, j)]
        
        return helper(0,0)

s = Solution()
s.uniquePaths(3,3)