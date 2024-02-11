# @leet start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        last_element = [-1]*n
        L = 1
        last_element[0] = 0
        for i in range(1, n):
            l,r = 0,L
            if nums[last_element[r-1]] < nums[i]:
                j = r
            else:
                while r-l > 1:
                    m = l + (r-l)//2
                    if nums[last_element[m - 1]] < nums[i]:
                        l = m
                    else:
                        r = m
                j = l

            if j == L or nums[i] < nums[last_element[j]]:
                last_element[j] = i
                L = max(L, j+1)
        return L


        
# @leet end
