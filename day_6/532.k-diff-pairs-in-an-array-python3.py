# @leet start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import defaultdict 
        if k == 0:
            s = defaultdict(int)
            for i in nums: s[i] += 1
            return sum(j>1 for j in s.values())

        srted = sorted(set(nums))
        i = 0
        ans = 0
        for j in range(len(srted)):
            d = srted[j] - srted[i]
            if d == k: 
                while i <= j and srted[j] - srted[i] == k: ans += 1;i += 1
            if d > k:
                while (i <= j) and srted[j] - srted[i] > k: i += 1
                if srted[j]-srted[i] == k: ans += 1
            else:
                continue
        return ans




# @leet end
