# @leet start
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        res = 0

        max_left, max_right = 0,0

        while l <= r:
            if (height[l] <= height[r]):
                if height[l] >= max_left: max_left = height[l]
                else:
                    res += max_left - height[l]
                l += 1
            else:
                if height[r] >= max_right: max_right = height[r]
                else:
                    res += max_right - height[r]
                r -= 1
        return res

# @leet end
