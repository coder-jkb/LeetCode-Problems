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
                    
        '''
        while i<nrows:
            j=0
            while j<ncolumns and i<nrows:
                print(i,j, matrix[i][j])
                if matrix[i][j] == 0:
                    # make column zero
                    for r in range(nrows):
                        matrix[r][j] = 0
                        
                    # make row zero
                    for c in range(ncolumns):
                        matrix[i][c] = 0
                        
                    i+=1; j+=1 # move diagonally
                else:
                    j+=1
            i+=1
        '''