# @leet start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [k for k in board[i] if k != '.']
            column = [board[j][i] for j in range(9) if board[j][i] != '.']
            
            x,y = divmod(i,3)
            box = [board[3*x+k][3*y+l] for k in range(3) for l in range(3) if board[3*x+k][3*y+l] != '.']
            
            for j in [row, column, box]:
                if len(j) != len(set(j)): return False
        return True
                
# @leet end
