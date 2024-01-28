# @leet start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        for i in sorted(intervals):
            l,r = i
            # last_interval = ans[-1]
            if ans and l <= ans[-1][-1]: 
                # the intervals overlap
                ans[-1][-1] = max(ans[-1][-1], r)
            else: 
                # disjoint intervals
                ans.append(i)
        return ans

        
# @leet end
