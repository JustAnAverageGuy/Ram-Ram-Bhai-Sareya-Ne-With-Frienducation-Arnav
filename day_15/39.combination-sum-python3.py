# @leet start
class Solution:
    def dfs(self, nums, target, path, ret):
        if target < 0: return
        if target == 0: ret.append(path); return
        for i in range(len(nums)):
            extra = target - nums[i]
            current_path = path + [nums[i]]
            self.dfs(nums[i:], extra, current_path, ret)
        return 

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret  = []
        self.dfs(candidates, target, [], ret)
        return ret
# @leet end
