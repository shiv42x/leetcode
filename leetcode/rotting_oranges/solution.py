from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        n, m = len(grid[0]), len(grid)
        directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]
        fresh_cnt = 0
        minutes = 0
        bfs_queue = deque()

        # populate fresh count and rotten set
        for row in range(m):
            for col in range(n):
                if grid[row][col] == FRESH:
                    fresh_cnt += 1
                elif grid[row][col] == ROTTEN:
                    bfs_queue.append((row, col))
        
        while bfs_queue and fresh_cnt > 0:
            for i in range(len(bfs_queue)):
                current_orange = bfs_queue.popleft()
                for direction in directions:
                    neighbour_row, neighbour_col = current_orange[0] + direction[0], current_orange[1] + direction[1]
                    # check out of bounds, or empty, or already rotten, or already visited
                    if neighbour_row < 0 or neighbour_row == m or neighbour_col < 0 or neighbour_col == n or grid[neighbour_row][neighbour_col] != FRESH:
                        continue
                    
                    grid[neighbour_row][neighbour_col] = 2
                    bfs_queue.append((neighbour_row, neighbour_col))
                    fresh_cnt -= 1
            minutes += 1
        
        return minutes if fresh_cnt == 0 else -1