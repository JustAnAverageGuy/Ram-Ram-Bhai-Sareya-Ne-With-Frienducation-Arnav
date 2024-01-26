# @leet start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_idx_qu = deque()
        ans = []
        for i in range(len(nums)):
            while max_idx_qu and nums[max_idx_qu[-1]] < nums[i]: max_idx_qu.pop() # remove smaller elements from the que
            
            max_idx_qu.append(i)

            if max_idx_qu[0] <= i - k: max_idx_qu.popleft() # if the max is further than k, remove it
            
            if i >= k-1: ans.append(nums[max_idx_qu[0]]) # collect the answers after atleast k elements have been taken
        
        return ans
        
# @leet end
