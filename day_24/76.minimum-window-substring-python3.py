# @leet start
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = defaultdict(int)
        for i in t: t_cnt[i] += 1
        missing = len(t_cnt)
        
        s_cnt = defaultdict(int)
        
        l = 0
        
        min_len = float('inf')
        
        answer_indices = [0,-1]

        for r in range(len(s)):
            s_cnt[s[r]] += 1
            
            missing -= (t_cnt[s[r]] and t_cnt[s[r]] == s_cnt[s[r]])    
            if missing: continue
            
            while True:
                x = s[l]
                if s_cnt[x] > t_cnt[x]:
                    s_cnt[x] -= 1
                    l += 1
                else:
                    break

            if r-l+1 < min_len:
                min_len = r-l+1
                answer_indices = [l,r]

        return s[answer_indices[0]:answer_indices[1]+1]


            
        
# @leet end
