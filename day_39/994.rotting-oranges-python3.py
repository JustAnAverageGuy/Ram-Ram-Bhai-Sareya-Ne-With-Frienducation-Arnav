# @leet start
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:  return -1
        n = len(grid[0])
        fresh = 0
        rotten = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while rotten and fresh > 0:
            time += 1
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    x, y = i + dx, j + dy
                    if x < 0 or x == m or y < 0 or y == n: continue
                    if grid[x][y] == 0 or grid[x][y] == 2: continue
                    fresh -= 1
                    grid[x][y] = 2
                    rotten.append((x, y))
        return time*(fresh==0)-(fresh>0)
# @leet end
