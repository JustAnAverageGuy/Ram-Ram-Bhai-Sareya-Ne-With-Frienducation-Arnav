# @leet start
class Solution:
    def reve(self, nums, i, j):
        # reverses nums[i:j+1]
        for x in range(i , (i+j+1)//2): nums[x], nums[i+j-x] = nums[i+j-x], nums[x]
        return

    def nextPermutation(self, nums: List[int]) -> None:
        # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        n = len(nums)
        
        for k in range(n-2, -1, -1):
            if nums[k] < nums[k+1]: break
        else:
            self.reve(nums, 0, n-1)
            return

        l = n-1
        for l in range(n-1, k,-1):
            if nums[k] < nums[l]: break
        
        nums[k], nums[l] =  nums[l], nums[k]
        
        self.reve(nums, k+1, n-1)
        
        return
# @leet end
