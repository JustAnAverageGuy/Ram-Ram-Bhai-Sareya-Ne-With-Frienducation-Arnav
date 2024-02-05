# @leet start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        A = [0]*m
        A[0] = 1 - obstacleGrid[0][0]
        for i in range(1,m):
            if obstacleGrid[0][i]: A[i] = 0
            else: A[i] = A[i-1]

        for j in range(1,n):
            if obstacleGrid[j][0]: A[0] = 0
            for i in range(1,m):
                if obstacleGrid[j][i]: A[i] = 0
                else: A[i] += A[i-1]
        return A[-1]
            
        
# @leet end
