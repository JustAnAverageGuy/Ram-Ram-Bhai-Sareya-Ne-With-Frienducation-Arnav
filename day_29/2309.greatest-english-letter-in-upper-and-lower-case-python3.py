# @leet start
class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]
        low = {i.lower():0 for i in alphabet}
        high = {i:0 for i in alphabet}
        for i in s:
            if i.islower():
                low[i] |= 1
            else:
                high[i]|= 1
        for x,y in zip(alphabet, alphabet.lower()):
            if high[x] and low[y]: return x
        return ""
        
# @leet end
