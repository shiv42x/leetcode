class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            for col in range(row, COLS):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp

        for row in matrix:
            row.reverse()

        return matrix