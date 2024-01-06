# @leet start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        in_array = {i : False for i in range(-100,101)}
        for i in nums: in_array[i] = True
        ok = [i for i in range(-100,101) if in_array[i]]
        for i in range(len(ok)):
            nums[i] = ok[i]
        return len(ok)
# @leet end
