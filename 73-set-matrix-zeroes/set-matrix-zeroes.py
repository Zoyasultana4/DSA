class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

    # Use the first row and first column to mark rows and columns to be zeroed.
    # We need a separate variable for matrix[0][0] as it serves for both
    # the first row and the first column.
        first_row_has_zero = False
        first_col_has_zero = False

    # Check if the first row needs to be zeroed
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

    # Check if the first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

    # Mark rows and columns using the first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the corresponding row
                    matrix[0][j] = 0  # Mark the corresponding column

    # Apply the zeroing based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    # Apply zeroing for the first row and column if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

# Example usage:
##matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
#setZeroes(matrix1)
#print(matrix1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

#matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
#setZeroes(matrix2)
#print(matrix2)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]