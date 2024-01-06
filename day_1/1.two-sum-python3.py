# @leet start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen_dict = dict()
        for i in range(n):
            complement = target - nums[i]
            if complement in seen_dict: return [seen_dict[complement], i]
            seen_dict[nums[i]] = i
        return []
# @leet end
