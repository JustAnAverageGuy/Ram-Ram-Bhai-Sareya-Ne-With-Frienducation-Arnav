# @leet start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [0]*n
        stk = [0]
        
        while stk:
            idx = stk.pop()

            if visited[idx] == 2: continue
            
            visited[idx] = 2
            rang = nums[idx]
            if idx + rang >= n-1: return True

            for k in range(min(idx + rang + 1, n)-1, idx, -1):
                if not visited[k]:
                    visited[k] = 1
                    stk.append(k)
        return False

            
        
# @leet end
