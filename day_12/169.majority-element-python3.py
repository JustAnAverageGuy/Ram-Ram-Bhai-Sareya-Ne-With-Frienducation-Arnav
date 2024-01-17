# @leet start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        return sorted(nums)[n//2]
# @leet end
