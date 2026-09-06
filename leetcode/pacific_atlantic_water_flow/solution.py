class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def _dfs(row, col, visited, prev_height):
            if ((row, col) in visited or
                row < 0 or col < 0 or row == ROWS or col == COLS or
                heights[row][col] < prev_height):
                return
            visited.add((row, col))
            _dfs(row + 1, col, visited, heights[row][col])
            _dfs(row - 1, col, visited, heights[row][col])
            _dfs(row, col + 1, visited, heights[row][col])
            _dfs(row, col - 1, visited, heights[row][col])

        for col in range(COLS):
           _dfs(0, col, pac, heights[0][col])
           _dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])

        for row in range(ROWS):
            _dfs(row, 0, pac, heights[row][0])
            _dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if ((i, j) in pac and (i, j) in atl):
                    result.append([i, j])
        return result