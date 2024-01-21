# @leet start
from itertools import combinations, chain
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = list(nums)
        # from pydocs
        return list(map(list, chain.from_iterable(combinations(s,r)  for r in range(len(s) + 1))))
        # another straightforward solution would have been to iterate from 0 to (1<<n)-1, and treat it as a mask

# @leet end
