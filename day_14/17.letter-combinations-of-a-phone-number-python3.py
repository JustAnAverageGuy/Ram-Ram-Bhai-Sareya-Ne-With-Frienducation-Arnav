# @leet start
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        keypad = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        s = [keypad[i] for i in digits]
        return list("".join(i) for i in product(*s))
# @leet end
