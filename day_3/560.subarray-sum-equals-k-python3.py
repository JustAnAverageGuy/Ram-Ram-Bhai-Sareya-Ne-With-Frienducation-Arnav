# @leet start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        pref = [0] # pref[i] = sum of first i elements of nums
        for i in nums: pref.append(pref[-1] + i)
        cnt = 0
        seen = defaultdict(int)
        for pre in pref:
            cnt += seen[pre-k]
            seen[pre] += 1
        return cnt
            

        
# @leet end
