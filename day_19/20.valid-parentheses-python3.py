# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        pairs = {"(":")", "[":"]", "{":"}"}
        openers = set(pairs.keys())
        
        for i in s:
            if i in openers: stk.append(i)
            else: # i in closers
                if len(stk) == 0: return False
                k = stk.pop()
                if pairs[k] != i: return False
        if len(stk) > 0: return False
        return True
        
# @leet end
