# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [i.lower() for i in s if i.isalnum()]
        if len(filtered) < 2: return True
        return all(filtered[i] == filtered[-i-1] for i in range(len(filtered)//2))
        
# @leet end
