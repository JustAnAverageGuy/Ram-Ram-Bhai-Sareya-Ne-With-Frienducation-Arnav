# @leet start
from functools import cache

S = ["","",""]
class Solution:

    @cache
    def dp(self, i,j):
        if j >= 0:
            if S[1][j] == S[2][i+j+1]:
                if self.dp(i, j-1): return True
        if i >= 0:
            if S[0][i] == S[2][i+j+1]:
                if self.dp(i-1, j): return True
        return (i==-1) and (j==-1)
        
         

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        global S
        S[0] = s1
        S[1] = s2
        S[2] = s3
        if len(s1)+len(s2) != len(s3): return False
        t =  self.dp(len(s1)-1,len(s2)-1)
        self.dp.cache_clear()
        return t
        
        
# @leet end
