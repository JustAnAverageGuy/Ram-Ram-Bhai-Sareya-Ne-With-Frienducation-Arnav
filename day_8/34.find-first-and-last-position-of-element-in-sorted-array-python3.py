# @leet start
from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # why reinvent the wheel

        left  =  bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        if left >= len(nums) or nums[left]  != target: return [-1, -1]
        if right < 0         or nums[right] != target: return [-1, -1]
        return [left, right]
        
        
# @leet end
