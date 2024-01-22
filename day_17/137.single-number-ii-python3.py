# @leet start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # mod 3 counter
        a,b = 0,0
        for c in nums: a,b =(~a&b&c)|(a&~b&~c), (~a&~b&c)|(~a&b&~c)
        return a|b
        
# @leet end
