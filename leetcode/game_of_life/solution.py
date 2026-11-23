class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        # Temporary state encoding:
        # 0: dead -> dead
        # 1: live -> live
        # 2: live -> dead  (was alive, will die)
        # 3: dead -> live  (was dead, will become alive)
        
        def count_live_neighbors(r: int, c: int) -> int:
            live_neighbors = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] in (1, 2):
                            live_neighbors += 1
            return live_neighbors

        for r in range(rows):
            for c in range(cols):
                neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[r][c] = 2  
                else:
                    if neighbors == 3:
                        board[r][c] = 3 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1