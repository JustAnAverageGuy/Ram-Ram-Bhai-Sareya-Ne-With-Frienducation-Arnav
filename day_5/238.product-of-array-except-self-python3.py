# @leet start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] # prefix[i] = prod[0,1,..,i-1]
        suffix = [1] # suffix[i] = prod[n-i,..,n-1]
        # ans[k] = prefix[k] * suffix[n-k-1]
        for i in range(1,n): prefix.append(prefix[-1] * nums[i-1])
        for i in range(1,n): suffix.append(suffix[-1] * nums[n-i])
        return [prefix[k]*suffix[n-k-1] for k in range(n)]
# @leet end
