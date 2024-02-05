# @leet start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for r in range(1,n):
            triangle[r][0] += triangle[r-1][0]
            for j in range(1,r): triangle[r][j] += min(triangle[r-1][j], triangle[r-1][j-1])
            triangle[r][r] += triangle[r-1][r-1]
        return min(triangle[-1])
# @leet end
