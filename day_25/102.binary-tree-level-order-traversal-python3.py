# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        qu = deque([(root,0)])
        ans = []
        
        while qu:
            node, depth = qu.popleft()
            if node is None: continue
            if len(ans) <= depth:
                ans.extend([] for i in range(depth - len(ans) + 1))
            ans[depth].append(node.val)
            if node.left is not None:
                qu.append((node.left, depth+1))
            if node.right is not None:
                qu.append((node.right, depth+1))

        return ans

        
# @leet end
