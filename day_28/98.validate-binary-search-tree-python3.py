# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        stk = [(root, float('-inf'), float('inf'))]
        while stk:
            node, lower_bound, upper_bound = stk.pop()
            if not (lower_bound < node.val < upper_bound): return False
            if node.right: stk.append((node.right, max(lower_bound, node.val), upper_bound))
            if node.left: stk.append((node.left, lower_bound, min(upper_bound, node.val)))
        return True
        
        
# @leet end
