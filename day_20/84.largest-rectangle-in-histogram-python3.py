# @leet start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        indices = [-1]
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[indices[-1]]:
                h = heights[indices.pop()]
                w = i - indices[-1] - 1
                ans = max(ans, h*w)
            indices.append(i)
            # print(*(heights[i] for i in indices))
        return ans
        
# @leet end 
