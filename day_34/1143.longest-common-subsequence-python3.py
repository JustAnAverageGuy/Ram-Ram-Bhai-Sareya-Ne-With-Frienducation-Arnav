from functools import cache
# @leet start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i,j):
            # return len of lcs in text1[:i] and text2[:j] 
            if i*j == 0: return 0
            return max( (1+dp(i-1, j-1)) if text1[i-1] == text2[j-1] else 0, dp(i,j-1), dp(i-1,j))
        return dp(len(text1), len(text2))
        
# @leet end
