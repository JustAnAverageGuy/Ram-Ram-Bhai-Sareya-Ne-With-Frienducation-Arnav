# @leet start
class Solution:
    def check(self, board, i, j, val):
        ro = 3*(i//3)
        col = 3*(j//3)
        for x in range(9):
            if val in [board[i][x], board[x][j], board[ro + x//3][col + x%3]]: return False
        return True 
    
    def dfs(self, board, i, j):
        if (i == 9): return True
        if (j == 9): return self.dfs(board, i+1, 0)
        if board[i][j] != '.':
            return self.dfs(board, i, j+1)
        for c in range(1, 10):
            if self.check(board, i, j, str(c)):
                board[i][j] = str(c)
                if self.dfs(board, i, j+1): return True
                board[i][j] = '.'
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.dfs(board, 0, 0)
        return
# @leet end
