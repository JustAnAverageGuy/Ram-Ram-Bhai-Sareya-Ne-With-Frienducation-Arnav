# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stk = [(root, 1)]
        max_depth = 0
        while stk:
            node, depth = stk.pop()
            if node is None: continue
            max_depth = max(max_depth, depth)
            if node.left is not None: stk.append((node.left, depth+1))
            if node.right is not None: stk.append((node.right, depth+1))
        return max_depth
# @leet end
