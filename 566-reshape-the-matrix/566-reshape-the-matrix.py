class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:          
        
        r0, c0 = len(mat), len(mat[0])
        if r0*c0 != r*c: # reshaping not possible
            return mat 
        
        # if reshaping is possible
        ans = [[0 for _ in range(c)] for _ in range(r)]
        
        i, j = 0, 0 # 
        for row in range(r0):
            for col in range(c0):
                ans[i][j] = mat[row][col]
                j+=1
                if j==c:
                    j=0
                    i+=1

        return ans
            
                