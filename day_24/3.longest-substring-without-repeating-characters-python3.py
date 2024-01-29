# @leet start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_indices = defaultdict(lambda : -1)
        max_cnt = 0
        curr_cint = 0

        for i, c in enumerate(s):
            if last_indices[c] == -1:
                curr_cint += 1
            else:
                curr_cint = min(i - last_indices[c], curr_cint + 1)

            last_indices[c] = i
            max_cnt = max(max_cnt, curr_cint)
        return max_cnt

        
        
# @leet end
