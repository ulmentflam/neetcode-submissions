class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows:int
        cols: int
        w: int = len(word)
        rows, cols = len(board), len(board[0])
        MARKER = '#'

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == w:
                return True
            if r < 0 or c < 0:
                return False
            if r >= rows or c >= cols:
                return False
            if board[r][c] == MARKER:
                return False
            if board[r][c] != word[idx]:
                return False
            
            board[r][c] = MARKER            
            res = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or 
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )
            board[r][c] = word[idx]
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
            