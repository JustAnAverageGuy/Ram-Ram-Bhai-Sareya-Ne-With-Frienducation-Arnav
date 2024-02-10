# @leet start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # @cache
        # def dp(i,j):
        #     # return len of lcs in text1[:i] and text2[:j] 
        #     if i*j == 0: return 0
        #     return max( (1+dp(i-1, j-1)) if text1[i-1] == text2[j-1] else 0, dp(i,j-1), dp(i-1,j))
        # return dp(len(text1), len(text2))

        text1, text2 = sorted((text1, text2), key=len)
        dp = [int(text1[0] == text2[0])]

        for c in range(1, len(text1)): dp.append(int(text1[c] == text2[0]) or dp[c-1])
        for j in range(1,len(text2)):
            prev = dp[0]
            dp[0] = dp[0] or int(text1[0] == text2[j])
            for c in range(1, len(text1)): dp[c],prev = max(dp[c], dp[c-1], (1+prev)*(text1[c] == text2[j])),dp[c]

        return dp[-1]


        
# @leet end
