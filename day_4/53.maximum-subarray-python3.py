# @leet start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_pre = [nums[0]]
        for i in nums[1:]:
            max_ending_here = i + max(max_pre[-1], 0) 
            max_pre.append(max_ending_here)
        return max(max_pre)

# @leet end
