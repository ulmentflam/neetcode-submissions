class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        MARK = '%'

        def dfs(row: int, col: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if (
                row < 0 or 
                col < 0 or 
                row >= M or 
                col >= N or 
                word[idx] != board[row][col] or 
                board[row][col] == MARK
                ):
                return False
            
            board[row][col] = MARK
            res = (
                dfs(row + 1, col, idx + 1) or
                dfs(row - 1, col, idx + 1) or
                dfs(row, col + 1, idx + 1) or
                dfs(row, col - 1, idx + 1)
            )
            board[row][col] = word[idx]
            return res
        
        for r in range(M):
            for c in range(N):
                if dfs(r, c, 0):
                    return True
        return False