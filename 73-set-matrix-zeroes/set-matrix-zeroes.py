class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        
        # Determine if the first row or first column needs to be zeroed
        first_row_has_zero = False
        first_col_has_zero = False

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use the first row and first column to mark zeroes
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeroes based on the marks in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0