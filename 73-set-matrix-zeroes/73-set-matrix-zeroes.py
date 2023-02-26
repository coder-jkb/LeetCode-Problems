class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows, ncols = len(matrix), len(matrix[0])
        zeros = dict()
        zeros['rows'] = set()
        zeros['cols'] = set()
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    zeros['rows'].add(i)
                    zeros['cols'].add(j)
                    
        for row in range(nrows):
            for col in range(ncols):
                if row in zeros['rows'] or col in zeros['cols']:
                    matrix[row][col] = 0
