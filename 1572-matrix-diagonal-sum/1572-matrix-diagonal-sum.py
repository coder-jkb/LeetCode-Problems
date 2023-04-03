class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        digsum =  0
        for i in range(N):
            digsum += mat[i][i] + mat[i][N-i-1]
            
        if N % 2 == 0:
            return digsum
        
        return digsum - mat[N//2][N//2]