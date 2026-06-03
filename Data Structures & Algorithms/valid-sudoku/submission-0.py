class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        I believe the naieve way to validate sodoku would be to iterate through all the rows, colums,
        and sub-grids. 

        This results in duplicated work, if you make one pass for rows and one pass for columns, and one pass for subgrids.

        So we need to check the same row, same column, same 3x3 box.
        """
        col, row = len(board), len(board[0]) # Valid because it's guarnteed to be a 9x9
        assert col == 9 and row == 9, "Not a 9x9 Grid"
        
        rows: dict[int, set[int]] = {} # Tracks digits seen in a row
        cols: dict[int, set[int]] = {} # Tracks digits seen in a column
        grids: dict[tuple[int, int], set[int]] = {} # Tracks digits in the 3 x 3 grid

        for i in range(col):
            for j in range(row):
                value: str = board[i][j]

                if not rows.get(j):
                    rows[j] = set([])
                
                if not cols.get(i):
                    cols[i] = set([])

                grid_idx: tuple[int, int] = (i // 3, j // 3)
                if not grids.get(grid_idx):
                    grids[grid_idx] = set([])
                
                if value == ".":
                    continue

                if value in rows[j]:
                    return False
                rows[j].add(value)

                if value in cols[i]:
                    return False
                cols[i].add(value)

                if value in grids[grid_idx]:
                    return False
                grids[grid_idx].add(value)

        return True

                


        