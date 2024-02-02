# @leet start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = [(root, float('-inf'), float('inf'))]
        while stk:
            node, lower_bound, upper_bound = stk.pop()
            if node is None: continue
            if not (lower_bound < node.val < upper_bound): return False
            stk.append((node.right, max(lower_bound, node.val), upper_bound))
            stk.append((node.left, lower_bound, min(upper_bound, node.val)))
        return True
        
        
# @leet end
