# @leet start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # linear in numer_of_rows + number_of_columns
        m, n = len(matrix), (len(matrix) and len(matrix[0]))
        r, c = 0, n-1
        while r < m and c >= 0:
            if   target > matrix[r][c]: r += 1
            elif target < matrix[r][c]: c -= 1
            else: return True
        return False        
# @leet end
