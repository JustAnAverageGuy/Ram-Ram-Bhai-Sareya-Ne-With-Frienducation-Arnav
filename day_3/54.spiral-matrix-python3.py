# @leet start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans.extend(matrix[0])
            matrix = [
                [ matrix[ro][col] for ro in range(1, len(matrix))] for col in range(len(matrix[0])-1,-1,-1)
            ] # adds the first row, then transposes the remaining matrix
        return ans

# @leet end
