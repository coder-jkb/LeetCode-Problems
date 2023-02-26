class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i=0; j=0
        nrows, ncols = len(matrix), len(matrix[0])
        zeros = dict()
        zeros['rows'] = set()
        zeros['cols'] = set()
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    zeros['rows'].add(i)
                    zeros['cols'].add(j)
            
        for row in list(zeros['rows']):
            for col in range(ncols):
                matrix[row][col] = 0
                
        for col in list(zeros['cols']):
            for row in range(nrows):
                matrix[row][col] = 0
