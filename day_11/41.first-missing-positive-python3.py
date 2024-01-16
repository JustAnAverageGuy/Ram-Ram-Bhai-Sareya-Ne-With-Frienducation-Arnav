# @leet start
# a hack
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for passes in range(5):
            for i in range(n):
                if 1 <= nums[i] <= n:
                    nums[ nums[i] - 1 ], nums[i] = nums[i], nums[nums[i] - 1]
        for k in range(n):
            if nums[k] != k+1: return k+1
        return n+1


# @leet end

