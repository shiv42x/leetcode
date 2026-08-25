class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        solved = False

        def map_to_box(row, col):
            return ((row // 3) * 3 + col // 3)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[map_to_box(i, j)].add(num)
        
        def solve(i, j):
            if i == 9:
                return True

            # (0, 8) -> (1, 0)
            next_i = i + (j + 1) // 9
            next_j = (j + 1) % 9
            
            if board[i][j] != '.':
                return solve(next_i, next_j)
            else:
                for guess in range(1, 10):
                    box_id = map_to_box(i, j)
                    if guess not in rows[i] and guess not in cols[j] and guess not in boxes[box_id]:
                        rows[i].add(guess)
                        cols[j].add(guess)
                        boxes[box_id].add(guess)
                        board[i][j] = str(guess)
                        result = solve(next_i, next_j)

                        if result:
                            return True
                        
                        # backtracking did not work
                        if not result:
                            rows[i].remove(guess)
                            cols[j].remove(guess)
                            boxes[box_id].remove(guess)
                            board[i][j] = '.'

        solve(0, 0)
        return board