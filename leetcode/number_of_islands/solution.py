class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(row, col):
            q = deque()
            visit.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and 
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in visit:
                    bfs(row, col)
                    islands += 1
        
        return islands
